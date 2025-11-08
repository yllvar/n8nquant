# Best Execution Monitor

## 📋 Overview
Monitors trade execution quality, calculates slippage, and ensures compliance with best execution obligations

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
| path | string | No | trade-execution-webhook | From Trade Execution Webhook node |

### Node-Specific Settings
- **Trade Execution Webhook** (n8n-nodes-base.webhook):
  - `events`: ['trade-execution']
  - `path`: trade-execution-webhook
  - `options`: {'responseMode': 'lastNode'}
- **Fetch Benchmark Price Data** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    symbol,
    AVG(price) as benchmark_price,
    AVG(volume) as benchmark_volume,
    MAX(...
- **Calculate Execution Quality Metrics** (n8n-nodes-base.code):
  - `functionCode`: // Calculate execution quality metrics
const calculateExecutionQuality = (trade, benchmark) => {
  c...
- **Store Execution Quality Data** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: execution_quality
  - `columns`: {'trade_id': '={{ $json.trade_id }}', 'symbol': '={{ $json.symbol }}', 'side': '={{ $json.side }}', ...
- **Check Execution Quality Rating** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Poor Execution Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_COMPLIANCE_CHANNEL }}
  - `text`: ⚠️ POOR EXECUTION QUALITY ALERT
• Trade ID: {{ $json.trade_id }}
• Symbol: {{ $json.symbol }}
• Side...
- **Generate Execution Quality Summary** (n8n-nodes-base.code):
  - `functionCode`: // Generate daily execution quality summary
const generateSummary = (executionData) => {
  const tot...
- **Email Execution Quality Report** (n8n-nodes-base.email):
  - `subject`: Daily Best Execution Report - {{ $json.date }}
  - `body`: Execution Quality Summary:
• Total Executions: {{ $json.total_executions }}
• Poor Execution Count: ...
  - `to`: ={{ $vars.COMPLIANCE_TEAM_EMAIL }}


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
