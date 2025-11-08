# Margin Call Processor

## 📋 Overview
Automates margin call processing, liquidation prioritization, and collateral management

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
| path | string | No | margin-call-webhook | From Margin Call Webhook Trigger node |
| method | string | No | POST | From Execute Liquidation Order node |
| nodeCredentialType | string | No | httpHeaderAuth | From Execute Liquidation Order node |

### Node-Specific Settings
- **Margin Call Webhook Trigger** (n8n-nodes-base.webhook):
  - `events`: ['margin-call']
  - `path`: margin-call-webhook
  - `options`: {'responseMode': 'lastNode'}
- **Fetch Account Status and Positions** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    a.account_id,
    a.account_number,
    a.client_name,
    a.margin_requirement,
    a.a...
- **Calculate Liquidation Plan** (n8n-nodes-base.code):
  - `functionCode`: // Calculate liquidation requirements and prioritize assets
const calculateLiquidation = (accountDat...
- **Check Liquidation Needed** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Execute Liquidation Order** (n8n-nodes-base.httpRequest):
  - `method`: POST
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.TRADING_API_KEY }}'}, {'name': '...
  - `body`: {'symbol': '={{ $json.liquidation_targets[0].symbol }}', 'side': 'SELL', 'quantity': '={{ $json.liqu...
  - `options`: {'timeout': 10000}
- **Update Account Status** (n8n-nodes-base.postgres):
  - `operation`: update
  - `table`: accounts
  - `columns`: {'margin_call_status': 'RESOLVED', 'last_liquidation_date': '={{ new Date().toISOString() }}', 'marg...
  - `additionalFields`: {'where': {'conditions': [{'column': 'account_id', 'value': '={{ $json.account_id }}'}]}}
- **Send Liquidation Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_TREASURY_CHANNEL }}
  - `text`: 💰 MARGIN CALL PROCESSED
• Account: {{ $json.account_number }}
• Client: {{ $json.client_name }}
• Sh...
- **Log Margin Call Processing** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: margin_call_logs
  - `columns`: {'account_id': '={{ $json.account_id }}', 'margin_requirement': '={{ $json.margin_requirement }}', '...


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
