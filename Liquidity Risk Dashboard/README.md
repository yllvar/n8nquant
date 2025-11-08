# Liquidity Risk Dashboard

## 📋 Overview
Monitors real-time liquidity metrics, bid-ask spreads, and market depth with alerts for deteriorating liquidity conditions

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
- **Real-Time Monitoring Trigger (1-min)** (n8n-nodes-base.cron):
  - `rule`: {'interval': [1], 'hour': ['*'], 'minute': ['*']}
- **Fetch Real-Time Liquidity Data** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    symbol,
    bid_price,
    ask_price,
    last_price,
    volume,
    spread_percentage,...
- **Calculate Liquidity Risk Metrics** (n8n-nodes-base.code):
  - `functionCode`: // Calculate liquidity risk metrics
const calculateLiquidityMetrics = (liquidityData) => {
  const m...
- **Check Critical Liquidity Conditions** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Critical Liquidity Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RISK_CHANNEL }}
  - `text`: 🔴 CRITICAL LIQUIDITY ALERT
• Symbol: {{ $json.symbol }}
• Liquidity Score: {{ $json.liquidity_score....
- **Store Liquidity Metrics History** (n8n-nodes-base.postgres):
  - `operation`: upsert
  - `table`: liquidity_monitoring
  - `columns`: {'symbol': '={{ $json.symbol }}', 'liquidity_score': '={{ $json.liquidity_score }}', 'liquidity_rati...
  - `additionalFields`: {'updateKey': 'symbol'}
- **Calculate Portfolio-Level Liquidity** (n8n-nodes-base.code):
  - `functionCode`: // Calculate portfolio-level liquidity risk
const calculatePortfolioLiquidity = (liquidityMetrics, p...
- **Email Liquidity Risk Dashboard** (n8n-nodes-base.email):
  - `subject`: Liquidity Risk Dashboard - {{ $now }}
  - `body`: Real-Time Liquidity Risk Summary:

Portfolio Liquidity Overview:
• Portfolio Liquidity Score: {{ $js...
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
