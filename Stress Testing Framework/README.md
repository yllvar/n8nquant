# Stress Testing Framework

## 📋 Overview
Executes comprehensive stress tests using multiple historical and hypothetical scenarios to assess portfolio resilience

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
- **Daily Stress Testing Trigger** (n8n-nodes-base.cron):
  - `rule`: {'hour': ['6'], 'minute': ['0']}
- **Fetch Active Stress Scenarios** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    scenario_id,
    scenario_name,
    shock_parameters,
    active,
    scenario_type
FROM...
- **Fetch Current Portfolio Positions** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    p.portfolio_id,
    p.portfolio_name,
    pos.symbol,
    pos.quantity,
    pos.average_...
- **Execute Stress Test Scenarios** (n8n-nodes-base.code):
  - `functionCode`: // Stress testing engine core logic
const runStressTest = (scenarios, portfolio) => {
  const result...
- **Store Stress Test Results** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: stress_test_results
  - `columns`: {'scenario_id': '={{ $json.scenario_id }}', 'portfolio_id': '={{ $json.portfolio_id }}', 'total_pnl'...
- **Generate Stress Test Summary** (n8n-nodes-base.code):
  - `functionCode`: // Generate stress test summary
const summary = {
  date: new Date().toISOString().split('T')[0],
  ...
- **Email Stress Test Report** (n8n-nodes-base.email):
  - `subject`: Daily Stress Test Report - {{ $json.date }}
  - `body`: Stress Testing Summary:
• Total Scenarios Run: {{ $json.total_scenarios_run }}
• Worst Case P&L: ${{...
  - `to`: ={{ $vars.RISK_TEAM_EMAIL }}
- **Check for Negative Stress Results** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Stress Test Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RISK_CHANNEL }}
  - `text`: ⚠️ STRESS TEST ALERT
• Scenario: {{ $json.scenario_name }}
• Portfolio: {{ $json.portfolio_name }}
•...


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
