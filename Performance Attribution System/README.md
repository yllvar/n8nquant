# Performance Attribution System

## 📋 Overview
Calculates performance attribution by factors, sectors, and other dimensions to understand portfolio returns

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
- **Daily Performance Attribution Trigger** (n8n-nodes-base.cron):
  - `rule`: {'hour': ['18'], 'minute': ['0']}
- **Fetch Portfolio Positions and Data** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    p.portfolio_id,
    p.portfolio_name,
    pos.symbol,
    pos.quantity,
    pos.average_...
- **Fetch Factor Exposures Data** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    factor_name,
    factor_return,
    factor_loading,
    symbol
FROM factor_exposures 
WH...
- **Calculate Performance Attribution** (n8n-nodes-base.code):
  - `functionCode`: // Performance attribution calculation
const calculateAttribution = (portfolioData, factorData) => {...
- **Store Attribution Results** (n8n-nodes-base.postgres):
  - `operation`: insert
  - `table`: performance_attribution
  - `columns`: {'portfolio_id': '={{ $json.portfolio_id }}', 'portfolio_name': '={{ $json.portfolio_name }}', 'attr...
- **Generate Attribution Summary Report** (n8n-nodes-base.code):
  - `functionCode`: // Generate attribution summary report
const generateSummary = (attributionResults) => {
  const gro...
- **Email Attribution Report** (n8n-nodes-base.email):
  - `subject`: Performance Attribution Report - {{ $json.date }}
  - `body`: Performance Attribution Summary:
• Portfolios Analyzed: {{ $json.portfolios_analyzed }}

Portfolio D...
  - `to`: ={{ $vars.PORTFOLIO_MANAGERS_EMAIL }}


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
