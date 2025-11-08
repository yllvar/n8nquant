# Portfolio Risk Monitor - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - Hourly] --> B[PostgreSQL - Fetch Portfolio Data]
    A --> C[PostgreSQL - Fetch Historical Prices]
    B --> D[Code Node - Calculate VaR]
    C --> D
    D --> E[PostgreSQL - Store VaR Results]
    E --> F{Check VaR Breach}
    F -->|Breach| G[Slack - Send Alert]
    F -->|No Breach| H[Email - Daily Risk Report]
    D --> H
```

## Description
This diagram shows the Portfolio Risk Monitor workflow that runs hourly to calculate Value at Risk (VaR) and monitor for risk threshold breaches.

## Key Components
- **Scheduled Execution**: Runs every hour
- **Data Integration**: Fetches portfolio and market data
- **Risk Calculation**: Computes Value at Risk metrics
- **Alerting**: Notifies team of risk threshold breaches
- **Reporting**: Generates daily risk reports
