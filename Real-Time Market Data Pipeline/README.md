# Real-Time Market Data Pipeline

## 📋 Overview
Fetches real-time market data from multiple sources, validates, and stores in database with error handling and monitoring

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
| method | string | No | GET | From Fetch Market Data from API node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch Market Data from API node |

### Node-Specific Settings
- **5-Minute Market Data Trigger** (n8n-nodes-base.cron):
  - `rule`: {'interval': [5], 'hour': ['*'], 'minute': ['*']}
- **Fetch Market Data from API** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.MARKET_DATA_API_KEY }}'}]}
  - `queryParameters`: {'parameters': [{'name': 'symbols', 'value': "={{ 'AAPL,GOOGL,MSFT,TSLA,SPY' }}"}, {'name': 'fields'...
- **Validate Market Data Quality** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Store Validated Market Data** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: market_data_real_time
  - `columns`: {'symbol': '={{ $json.symbol }}', 'price': '={{ $json.price }}', 'bid_price': '={{ $json.bid }}', 'a...
- **Log Data Validation Errors** (n8n-nodes-base.set):
  - `mode`: item
  - `item`: {'json': {'error_type': 'Data Validation Failed', 'failed_symbol': '={{ $json.symbol }}', 'error_mes...
- **Send Slack Alert on Data Issues** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_ALERTS_CHANNEL }}
  - `text`: 🚨 Market Data Pipeline Alert
• Validation failed for symbol: {{ $json.failed_symbol }}
• Error: {{ $...
- **Calculate Pipeline Performance Metrics** (n8n-nodes-base.code):
  - `functionCode`: // Calculate pipeline metrics
const metrics = {
  total_records_processed: items.length,
  successfu...


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
