# Automated Backtesting Engine

## 📋 Overview
Comprehensive backtesting framework for quantitative strategies with performance metrics and walk-forward analysis

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
- **Manual Backtest Trigger** (n8n-nodes-base.manualTrigger):
- **Load Strategy Configurations** (n8n-nodes-base.code):
  - `functionCode`: // Strategy configuration
const strategies = [
  {
    strategy_id: 'momentum_1m',
    name: '1-Mont...
- **Fetch Historical Price Data for Universe** (n8n-nodes-base.postgres):
  - `sql`: SELECT symbol, date, open, high, low, close, volume
FROM historical_prices 
WHERE symbol IN (SELECT ...
  - `additionalFields`: {'queryParams': "={{ [\n  $json.universe,\n  '2018-01-01',\n  '2023-12-31'\n] }}"}
- **Execute Strategy Backtest** (n8n-nodes-base.code):
  - `functionCode`: // Backtesting engine core logic
const backtestStrategy = (strategy, priceData) => {
  const signals...
- **Calculate Performance Metrics** (n8n-nodes-base.code):
  - `functionCode`: // Calculate comprehensive performance metrics
const calculatePerformance = (backtestResult) => {
  ...
- **Store Backtest Results in Database** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: backtest_results
  - `columns`: {'strategy_id': '={{ $json.strategy_id }}', 'strategy_name': '={{ $json.strategy_name }}', 'total_tr...
- **Email Backtest Performance Report** (n8n-nodes-base.email):
  - `subject`: Backtest Results - {{ $json.strategy_name }} - {{ $now }}
  - `body`: Strategy Backtest Performance Report:

Strategy: {{ $json.strategy_name }}
Period: {{ $json.backtest...
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
