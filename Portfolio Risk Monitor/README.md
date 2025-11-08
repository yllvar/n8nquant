# Portfolio Risk Monitor

## 📋 Overview
Calculates Value at Risk (VaR) for portfolios using historical simulation, monitors breaches, and alerts risk team

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
No configurable parameters found.

### Node-Specific Settings
- **Hourly Risk Calculation Trigger** (n8n-nodes-base.cron):
  - `rule`: {'interval': [60], 'hour': ['9-17'], 'minute': ['0,30']}
- **Fetch Active Portfolio Positions** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    p.portfolio_id,
    p.portfolio_name,
    pos.symbol,
    pos.quantity,
    pos.average_...
- **Fetch 1-Year Historical Prices** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    symbol,
    date,
    close_price,
    LAG(close_price, 1) OVER (PARTITION BY symbol ORD...
- **Calculate Value at Risk (Historical Simulation)** (n8n-nodes-base.code):
  - `functionCode`: // VaR Calculation using Historical Simulation
const calculateVaR = (positions, historicalReturns, c...
- **Store VaR Results with Breach Status** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: risk_calculations
  - `columns`: {'portfolio_id': '={{ $json.portfolio_id }}', 'var_95': '={{ $json.var_95 }}', 'confidence_level': '...
- **Check VaR Limit Breach** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send VaR Breach Alert to Risk Team** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RISK_CHANNEL }}
  - `text`: 🔴 VAR LIMIT BREACH DETECTED
• Portfolio: {{ $json.portfolio_name }}
• Current VaR: ${{ $json.var_95....
- **Email Daily Risk Summary** (n8n-nodes-base.email):
  - `subject`: Daily Risk Report - {{ $now }}
  - `body`: Portfolio Risk Summary:

{{ $json.map(item => `Portfolio: ${item.portfolio_name}\nVaR (95%): $${item...
  - `to`: ={{ $vars.RISK_TEAM_EMAIL }}


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
