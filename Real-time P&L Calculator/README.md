# Real-time P&L Calculator

## 📋 Overview
Real-time P&L calculation engine that processes market price updates and calculates position valuations

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
| path | string | No | price-update-webhook | From Market Price Update Webhook node |

### Node-Specific Settings
- **Market Price Update Webhook** (n8n-nodes-base.webhook):
  - `events`: ['price-update']
  - `path`: price-update-webhook
  - `options`: {'responseMode': 'lastNode'}
- **Fetch Positions for Symbol** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    position_id,
    symbol,
    quantity,
    average_cost,
    portfolio_id,
    account_i...
- **Calculate Real-time P&L** (n8n-nodes-base.code):
  - `functionCode`: // Calculate real-time P&L for positions
const calculatePnL = (positions, marketData) => {
  const c...
- **Store P&L Calculations** (n8n-nodes-base.postgres):
  - `operation`: upsert
  - `table`: pnl_calculations
  - `columns`: {'position_id': '={{ $json.position_id }}', 'symbol': '={{ $json.symbol }}', 'quantity': '={{ $json....
  - `additionalFields`: {'updateKey': 'position_id'}
- **Publish P&L Update to Queue** (n8n-nodes-base.redis):
  - `topic`: pnl-updates
  - `message`: ={{ JSON.stringify($json) }}
- **Check Large P&L Movements** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Large P&L Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RISK_CHANNEL }}
  - `text`: 📊 LARGE P&L MOVEMENT ALERT
• Position: {{ $json.symbol }} ({{ $json.quantity }} shares)
• Current Pr...
- **Aggregate Portfolio-Level P&L** (n8n-nodes-base.code):
  - `functionCode`: // Aggregate portfolio-level P&L
const aggregatePortfolioPnL = (pnlData) => {
  const portfolioGroup...
- **Email P&L Summary** (n8n-nodes-base.email):
  - `subject`: Real-time P&L Dashboard - {{ $now }}
  - `body`: Portfolio P&L Summary:
{{ $json.map(portfolio => `
${portfolio.portfolio_id}:
• Total Unrealized P&L...
  - `to`: ={{ $vars.TRADING_TEAM_EMAIL }}


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
