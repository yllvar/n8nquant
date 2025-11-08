# Quant Strategy Deployment Pipeline

## 📋 Overview
Automated CI/CD pipeline for quantitative strategies with testing, validation, and deployment

## 🚀 Quick Start

### Prerequisites
- n8n instance (v1.0+ recommended)
- [List any specific requirements]

### Installation
1. **Import Workflow**
   - Download the workflow JSON file
   - In n8n, go to Workflows → Import from File
   - Select the downloaded JSON file

2. **Configure Credentials**
   - [List required credentials and how to set them up]
   - Example: API keys, database connections, etc.

3. **Environment Variables**
   ```env
   # Copy these to your .env file
   VARIABLE_NAME=value
   ```

## 🛠 Configuration

### Workflow Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| path | string | No | github-webhook | From GitHub Push Trigger node |

### Node-Specific Settings
- **GitHub Push Trigger** (n8n-nodes-base.webhook):
  - `events`: ['push']
  - `path`: github-webhook
  - `options`: {'responseMode': 'lastNode'}
- **Parse GitHub Event** (n8n-nodes-base.code):
  - `functionCode`: // Parse GitHub push event and extract strategy information
const githubEvent = $json;

if (githubEv...
- **Check if Deployment Should Proceed** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Run Unit Tests** (n8n-nodes-base.executeCommand):
  - `command`: cd /tmp/{{ $json.strategy_name }} && python -m pytest tests/ --junitxml=pytest.xml
  - `additionalParameters`: {'shell': 'bash'}
- **Check Unit Test Results** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Build Docker Image** (n8n-nodes-base.executeCommand):
  - `command`: cd /tmp/{{ $json.strategy_name }} && docker build -t quant-strategy:{{ $json.commit_hash }} .
  - `additionalParameters`: {'shell': 'bash'}
- **Run Backtest Validation** (n8n-nodes-base.executeCommand):
  - `command`: docker run --rm -e DB_HOST={{ $vars.DB_HOST }} -e API_KEY={{ $vars.API_KEY }} quant-strategy:{{ $jso...
  - `additionalParameters`: {'shell': 'bash'}
- **Publish Deployment Ready Event** (n8n-nodes-base.redis):
  - `topic`: strategy-deployment
  - `message`: {'strategy': '={{ $json.strategy_name }}', 'version': '={{ $json.commit_hash }}', 'status': 'ready-f...
- **Generate Deployment Summary** (n8n-nodes-base.code):
  - `functionCode`: // Generate deployment summary
const summary = {
  strategy_name: $json.strategy_name,
  commit_hash...
- **Send Deployment Ready Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RESEARCH_CHANNEL }}
  - `text`: 🚀 STRATEGY DEPLOYMENT READY
• Strategy: {{ $json.strategy_name }}
• Commit: {{ $json.commit_hash.sub...
- **Log Deployment Event** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: strategy_deployments
  - `columns`: {'strategy_name': '={{ $json.strategy_name }}', 'commit_hash': '={{ $json.commit_hash }}', 'branch':...


## 🏃‍♂️ Running the Workflow

### Manual Execution
1. Open the workflow in n8n
2. Click "Execute Node" on the trigger node
3. Monitor execution in the "Executions" tab

### Scheduled Execution
- **Cron Expression**: `0 * * * *` (runs every hour)
- Adjust the cron expression as needed

## 📊 Expected Output

### Successful Execution
- Description of successful output
- Example response:
  ```json
  {
    "status": "success",
    "data": {}
  }
  ```

### Error Handling
- Common error messages and resolutions
- How to interpret error codes

## 🔍 Monitoring & Maintenance

### Logging
- Logs can be viewed in the n8n Executions tab
- Each execution includes detailed logs for debugging

### Performance Metrics
- Average execution time: [Add expected time]
- Memory usage: [Add expected usage]

## 🔄 Version History

| Version | Date       | Changes                     |
|---------|------------|----------------------------|
| 1.0.0   | 2025-11-09 | Initial release             |


## 📝 Notes
- Any additional important information
- Known issues or limitations
- Links to related documentation
