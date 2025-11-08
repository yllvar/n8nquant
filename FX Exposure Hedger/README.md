# FX Exposure Hedger

## 📋 Overview
Automates foreign exchange exposure monitoring, hedge ratio calculation, and execution of hedging strategies with real-time FX rate monitoring

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
| method | string | No | GET | From Fetch Real-Time FX Rates node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch Real-Time FX Rates node |
| method | string | No | POST | From Execute FX Hedge Order node |
| nodeCredentialType | string | No | httpHeaderAuth | From Execute FX Hedge Order node |
| body | string | No | ={{
  {
    "order_type": "LIMIT",
    "currency_pair": $json.currency_pair,
    "side": $json.hedge_direction,
    "quantity": $json.notional_amount,
    "limit_price": $json.current_fx_rate,
    "time_in_force": "GTC",
    "strategy": "FX_HEDGE",
    "hedge_metadata": {
      "portfolio_id": $json.portfolio_id,
      "original_exposure": $json.original_exposure,
      "hedge_ratio": $json.hedge_ratio
    }
  }
}} | From Execute FX Hedge Order node |

### Node-Specific Settings
- **FX Exposure Monitoring Trigger** (n8n-nodes-base.cron):
  - `rule`: {'interval': [15], 'hour': ['6-22'], 'minute': ['0,15,30,45']}
- **Fetch Non-USD Currency Exposures** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    portfolio_id,
    currency,
    SUM(market_value) as total_exposure,
    COUNT(*) as pos...
- **Fetch Real-Time FX Rates** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.FX_API_KEY }}'}]}
  - `queryParameters`: {'parameters': [{'name': 'base', 'value': 'USD'}, {'name': 'symbols', 'value': 'EUR,GBP,JPY,CHF,CAD,...
- **Calculate Optimal Hedge Orders** (n8n-nodes-base.code):
  - `functionCode`: // Calculate optimal hedge ratios and generate hedge orders
const calculateHedgeRequirements = (expo...
- **Filter Hedge Orders Above Threshold** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Execute FX Hedge Order** (n8n-nodes-base.httpRequest):
  - `method`: POST
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.TRADING_API_KEY }}'}, {'name': '...
  - `body`: ={{
  {
    "order_type": "LIMIT",
    "currency_pair": $json.currency_pair,
    "side": $json.hedge...
  - `options`: {'timeout': 30000}
- **Store Hedge Order Record** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: fx_hedge_orders
  - `columns`: {'order_id': '={{ $json.order_id }}', 'portfolio_id': '={{ $json.portfolio_id }}', 'currency_pair': ...
- **Alert Treasury Team on Hedge Execution** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_TREASURY_CHANNEL }}
  - `text`: 🛡️ FX HEDGE EXECUTED
• Portfolio: {{ $json.portfolio_id }}
• Currency: {{ $json.currency_pair }}
• D...
- **Calculate Hedge Effectiveness** (n8n-nodes-base.code):
  - `functionCode`: // Calculate post-hedge exposure and effectiveness
const calculateHedgeEffectiveness = (hedgeOrders,...
- **Email Hedge Effectiveness Report** (n8n-nodes-base.email):
  - `subject`: FX Hedge Effectiveness Report - {{ $now }}
  - `body`: FX Exposure Hedging Effectiveness Report:

Portfolio Summary:
• Total Original Exposure: ${{ $json.p...
  - `to`: ={{ $vars.TREASURY_TEAM_EMAIL }}


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
