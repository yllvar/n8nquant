# Counterparty Risk Monitor

## 📋 Overview
Monitors counterparty exposures, calculates CVA, and alerts on deteriorating credit conditions

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
- **30-Minute Counterparty Risk Trigger** (n8n-nodes-base.cron):
  - `rule`: {'interval': [30], 'hour': ['*'], 'minute': ['*/30']}
- **Fetch Counterparty Exposures** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    cp.counterparty_id,
    cp.name,
    cp.rating,
    cp.cds_spread,
    cp.risk_weight,
 ...
- **Calculate CVA and Credit Risk Metrics** (n8n-nodes-base.code):
  - `functionCode`: // Calculate Credit Value Adjustment (CVA) and other risk metrics
const calculateCVA = (exposures) =...
- **Check High CVA Threshold** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Counterparty Risk Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RISK_CHANNEL }}
  - `text`: 🔴 HIGH COUNTERPARTY RISK ALERT
• Counterparty: {{ $json.name }}
• Rating: {{ $json.rating }}
• Total...
- **Store Counterparty Monitoring Data** (n8n-nodes-base.postgres):
  - `operation`: upsert
  - `table`: counterparty_risk_monitoring
  - `columns`: {'counterparty_id': '={{ $json.counterparty_id }}', 'name': '={{ $json.name }}', 'rating': '={{ $jso...
  - `additionalFields`: {'updateKey': 'counterparty_id'}
- **Generate Counterparty Risk Summary** (n8n-nodes-base.code):
  - `functionCode`: // Generate daily counterparty risk summary
const summary = {
  date: new Date().toISOString().split...
- **Email Counterparty Risk Summary** (n8n-nodes-base.email):
  - `subject`: Counterparty Risk Dashboard - {{ $now }}
  - `body`: Counterparty Risk Summary:
• Total Counterparties Monitored: {{ $json.total_counterparties_monitored...
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
