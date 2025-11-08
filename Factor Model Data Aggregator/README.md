# Factor Model Data Aggregator

## 📋 Overview
Aggregates and processes multi-source data for quantitative factor models including fundamental, macroeconomic, and technical factors

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
| method | string | No | GET | From Fetch Fundamental Data (Value Factors) node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch Fundamental Data (Value Factors) node |
| method | string | No | GET | From Fetch Macroeconomic Indicators node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch Macroeconomic Indicators node |

### Node-Specific Settings
- **Daily Factor Data Update Trigger** (n8n-nodes-base.cron):
  - `rule`: {'hour': ['6'], 'minute': ['0']}
- **Fetch Investment Universe Symbols** (n8n-nodes-base.postgres):
  - `sql`: SELECT DISTINCT symbol FROM universe_constituents WHERE active = true AND inclusion_date <= CURRENT_...
- **Fetch Fundamental Data (Value Factors)** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.FUNDAMENTAL_API_KEY }}'}]}
  - `queryParameters`: {'parameters': [{'name': 'symbols', 'value': "={{ items.map(item => item.json.symbol).slice(0, 100)....
- **Fetch Macroeconomic Indicators** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.MACRO_API_KEY }}'}]}
  - `queryParameters`: {'parameters': [{'name': 'indicators', 'value': 'GDP,CPI,UNEMPLOYMENT,INTEREST_RATES,CONSUMER_SENTIM...
- **Fetch Price Data for Momentum Factors** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    symbol,
    date,
    close_price,
    volume,
    LAG(close_price, 1) OVER (PARTITION B...
- **Calculate Factor Exposures & Scores** (n8n-nodes-base.code):
  - `functionCode`: // Calculate factor exposures and scores
const calculateFactorExposures = (fundamentalData, priceDat...
- **Store Factor Exposure Data** (n8n-nodes-base.postgres):
  - `operation`: upsert
  - `table`: factor_exposures
  - `columns`: {'symbol': '={{ $json.symbol }}', 'calculation_date': '={{ $json.date }}', 'value_score': '={{ $json...
  - `additionalFields`: {'updateKey': 'symbol,calculation_date'}
- **Generate Factor Analytics Report** (n8n-nodes-base.code):
  - `functionCode`: // Generate factor analytics and insights
const generateFactorAnalytics = (factorExposures) => {
  c...
- **Email Factor Data Update** (n8n-nodes-base.email):
  - `subject`: Factor Model Data Update - {{ $now }}
  - `body`: Quantitative Factor Model Data Update:

Coverage Summary:
• Total Symbols: {{ $json.total_symbols }}...
  - `to`: ={{ $vars.QUANT_RESEARCH_TEAM_EMAIL }}


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
