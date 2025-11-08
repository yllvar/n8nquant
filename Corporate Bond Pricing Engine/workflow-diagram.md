# Corporate Bond Pricing Engine - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - 15 min] --> B[HTTP Request - TRACE API]
    A --> C[PostgreSQL - Fetch Bond Metadata]
    B --> D[Code Node - Calculate Bond Prices]
    C --> D
    D --> E[PostgreSQL - Store Pricing Data]
    D --> F{Check Price Changes}
    F -->|Large Change| G[Slack - Price Alert]
    F -->|Normal Change| H[Code Node - Generate Summary]
    E --> H
    H --> I[Email - Pricing Report]
```

## Description
This diagram illustrates the Corporate Bond Pricing Engine workflow that updates bond prices and monitors for significant price movements.

## Key Components
- **Scheduled Execution**: Runs every 15 minutes
- **Market Data**: Fetches TRACE pricing data
- **Pricing Logic**: Calculates bond prices using market data
- **Data Storage**: Maintains historical price records
- **Alerting**: Notifies of significant price movements
- **Reporting**: Generates pricing reports
