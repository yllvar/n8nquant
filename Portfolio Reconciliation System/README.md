# Portfolio Reconciliation System

## 📋 Overview
Automates daily portfolio reconciliation between internal systems and prime brokers, identifies breaks, and initiates resolution workflows

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
| method | string | No | GET | From Fetch Prime Broker Positions node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch Prime Broker Positions node |

### Node-Specific Settings
- **End-of-Day Reconciliation Trigger** (n8n-nodes-base.cron):
  - `rule`: {'hour': ['18'], 'minute': ['30']}
- **Fetch Internal Portfolio Positions** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    portfolio_id,
    symbol,
    quantity,
    cost_basis,
    market_value,
    unrealized...
- **Fetch Prime Broker Positions** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.PRIME_BROKER_API_KEY }}'}, {'nam...
  - `queryParameters`: {'parameters': [{'name': 'as_of_date', 'value': "={{ new Date().toISOString().split('T')[0] }}"}]}
- **Reconcile Positions & Identify Breaks** (n8n-nodes-base.code):
  - `functionCode`: // Reconcile internal vs prime broker positions
const reconcilePositions = (internalPositions, broke...
- **Check for Critical Reconciliation Breaks** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Alert Ops Team on Critical Breaks** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_OPS_CHANNEL }}
  - `text`: 🔴 CRITICAL RECONCILIATION BREAKS
• Total Breaks: {{ $json.summary.breaks_found }}
• Critical Breaks:...
- **Store Reconciliation Breaks** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: reconciliation_breaks
  - `columns`: {'break_id': '={{ $json.break_id }}', 'symbol': '={{ $json.symbol }}', 'portfolio_id': '={{ $json.po...
- **Auto-Resolve Simple Breaks** (n8n-nodes-base.code):
  - `functionCode`: // Auto-resolve simple breaks (FX differences, rounding errors)
const autoResolveBreaks = (reconcili...
- **Update Auto-Resolved Breaks Status** (n8n-nodes-base.postgres):
  - `operation`: update
  - `table`: reconciliation_breaks
  - `columns`: {'status': 'RESOLVED', 'resolution_reason': '={{ $json.resolution_reason }}', 'resolved_at': '={{ $j...
  - `additionalFields`: {'where': {'conditions': [{'column': 'break_id', 'value': '={{ $json.break_id }}'}]}}
- **Email Reconciliation Summary Report** (n8n-nodes-base.email):
  - `subject`: Portfolio Reconciliation Summary - {{ $now }}
  - `body`: Daily Portfolio Reconciliation Report:

Summary:
• Internal Positions: {{ $json.summary.total_intern...
  - `to`: ={{ $vars.OPERATIONS_TEAM_EMAIL }}


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
