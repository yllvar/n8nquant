# Corporate Bond Pricing Engine

## 📋 Overview
Real-time corporate bond pricing engine with credit risk adjustment and liquidity factors

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
| method | string | No | GET | From Fetch TRACE Transaction Data node |
| nodeCredentialType | string | No | httpHeaderAuth | From Fetch TRACE Transaction Data node |

### Node-Specific Settings
- **15-Minute Bond Pricing Trigger** (n8n-nodes-base.cron):
  - `rule`: {'interval': [15], 'hour': ['*'], 'minute': ['*/15']}
- **Fetch TRACE Transaction Data** (n8n-nodes-base.httpRequest):
  - `method`: GET
  - `nodeCredentialType`: httpHeaderAuth
  - `sendHeaders`: True
  - `headerParameters`: {'parameters': [{'name': 'Authorization', 'value': 'Bearer {{ $vars.TRACE_API_KEY }}'}]}
  - `queryParameters`: {'parameters': [{'name': 'tradeType', 'value': 'ALL'}, {'name': 'timeRange', 'value': '1D'}]}
  - `options`: {'timeout': 20000}
- **Fetch Bond Metadata** (n8n-nodes-base.postgres):
  - `sql`: SELECT 
    bond_id,
    isin,
    issuer,
    coupon_rate,
    maturity_date,
    face_value,
    c...
- **Calculate Bond Prices and Greeks** (n8n-nodes-base.code):
  - `functionCode`: // Bond pricing engine with credit and liquidity adjustments
const priceBonds = (traceData, bondMeta...
- **Store Bond Pricing Data** (n8n-nodes-base.postgres):
  - `operation`: upsert
  - `table`: bond_prices
  - `columns`: {'bond_id': '={{ $json.bond_id }}', 'isin': '={{ $json.isin }}', 'clean_price': '={{ $json.clean_pri...
  - `additionalFields`: {'updateKey': 'bond_id'}
- **Check for Large Price Changes** (n8n-nodes-base.if):
  - `conditions`: {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict'}, 'conditions': [{'i...
- **Send Bond Price Alert** (n8n-nodes-base.slack):
  - `channel`: ={{ $vars.SLACK_RISK_CHANNEL }}
  - `text`: 📈 BOND PRICE ALERT
• ISIN: {{ $json.isin }}
• Issuer: {{ $json.issuer }}
• Clean Price: ${{ $json.cl...
- **Generate Bond Pricing Summary** (n8n-nodes-base.code):
  - `functionCode`: // Generate bond pricing summary
const summary = {
  date: new Date().toISOString().split('T')[0],
 ...
- **Email Bond Pricing Report** (n8n-nodes-base.email):
  - `subject`: Bond Pricing Report - {{ $json.date }}
  - `body`: Bond Pricing Summary:
• Bonds Priced: {{ $json.bonds_priced }}
• Average Price Change: ${{ $json.avg...
  - `to`: ={{ $vars.FIXED_INCOME_TEAM_EMAIL }}


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
