# Corporate Actions Processor

## 📋 Overview
Automates processing of corporate actions including dividends, stock splits, mergers, and spin-offs with position updates and cash reconciliation

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
| method | string | No | GET | From Fetch Corporate Actions Announcements node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch Corporate Actions Announcements node |

### Node-Specific Settings
- **Corporate Actions Monitoring Trigger** (n8n-nodes-base.cron):
  - `rule`: {'hour': ['7,12,17'], 'minute': ['0']}
- **Fetch Corporate Actions Announcements** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.CORP_ACTIONS_API_KEY }}'}, {'nam...
  - `queryParameters`: {'parameters': [{'name': 'from_date', 'value': "={{ new Date(Date.now() - 24 * 60 * 60 * 1000).toISO...
- **Fetch Active Portfolio Symbols** (n8n-nodes-base.postgres):
  - `sql`: SELECT DISTINCT symbol FROM portfolio_positions WHERE quantity != 0 AND active = true
- **Filter Relevant Corporate Actions** (n8n-nodes-base.code):
  - `functionCode`: // Filter corporate actions for portfolio holdings
const filterRelevantActions = (corpActions, portf...
- **Identify Dividend Actions** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Process Dividend Payments** (n8n-nodes-base.code):
  - `functionCode`: // Process dividend payments
const processDividendActions = (dividendActions) => {
  const dividendP...
- **Store Dividend Payment Records** (n8n-nodes-base.postgres):
  - `sql`: INSERT INTO dividend_payments (
  corporate_action_id, symbol, action_type, dividend_amount, 
  ex_d...
- **Identify Stock Split Actions** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Process Stock Splits** (n8n-nodes-base.code):
  - `functionCode`: // Process stock splits
const processStockSplits = (splitActions) => {
  const splitAdjustments = []...
- **Adjust Positions for Stock Splits** (n8n-nodes-base.postgres):
  - `sql`: UPDATE portfolio_positions 
SET quantity = quantity * {{ $json.adjustment_factor }},
    average_cos...
- **Generate Corporate Actions Summary** (n8n-nodes-base.code):
  - `functionCode`: // Generate corporate actions summary
const generateSummary = (relevantActions, processedDividends, ...
- **Email Corporate Actions Summary** (n8n-nodes-base.email):
  - `subject`: Corporate Actions Daily Summary - {{ $now }}
  - `body`: Corporate Actions Processing Summary:

• Total Actions: {{ $json.total_actions }}
• Critical Actions...
  - `to`: ={{ $vars.OPERATIONS_TEAM_EMAIL }}
- **Slack Alert for New Corporate Actions** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_OPERATIONS_CHANNEL }}
  - `text`: 📋 Corporate Actions Alert
• New actions detected: {{ items.length }}
• Critical actions: {{ items.fi...


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
