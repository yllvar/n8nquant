# Research Data Pipeline

## 📋 Overview
ETL pipeline for financial research data including news, sentiment, and alternative data sources

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
| method | string | No | GET | From Fetch Financial News from API node |
| nodeCredentialType | string | No | httpQueryAuth | From Fetch Financial News from API node |

### Node-Specific Settings
- **Hourly Research Data Trigger** (n8n-nodes-base.cron):
  - `rule`: {'interval': [60], 'hour': ['*'], 'minute': ['*/60']}
- **Fetch Financial News from API** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpQueryAuth
  - `sendHeaders`: True
  - `queryParameters`: {'parameters': [{'name': 'apiKey', 'value': '={{ $vars.NEWS_API_KEY }}'}, {'name': 'q', 'value': 'fi...
  - `options`: {'timeout': 15000}
- **Process News and Calculate Sentiment** (n8n-nodes-base.code):
  - `functionCode`: // Process news articles and calculate sentiment
const processNews = (articles) => {
  return articl...
- **Store Processed Research Data** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: research_data
  - `columns`: {'article_id': '={{ $json.article_id }}', 'title': '={{ $json.title }}', 'description': '={{ $json.d...
- **Publish Research Data to Queue** (n8n-nodes-base.redis):
  - `topic`: research-updates
  - `message`: ={{ JSON.stringify($json) }}
- **Check for Significant News Events** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Significant News Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RESEARCH_CHANNEL }}
  - `text`: 📢 SIGNIFICANT NEWS ALERT
• Title: {{ $json.title }}
• Sentiment: {{ $json.sentiment_score > 0 ? 'POS...
- **Calculate Research Pipeline Metrics** (n8n-nodes-base.code):
  - `functionCode`: // Calculate research pipeline metrics
const metrics = {
  total_articles_processed: items.length,
 ...


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
