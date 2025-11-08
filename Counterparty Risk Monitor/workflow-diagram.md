# Counterparty Risk Monitor - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - Hourly] --> B[PostgreSQL - Fetch Counterparty Data]
    A --> C[PostgreSQL - Fetch Exposures]
    A --> D[HTTP Request - Credit Ratings API]
    B --> E[Code Node - Calculate Risk Metrics]
    C --> E
    D --> E
    E --> F{Check High Risk Counterparties}
    E --> G{Check Margin Call Required}
    F -->|High Risk| H[Slack - Alert Credit Team]
    G -->|Margin Call| I[HTTP Request - Collateral API]
    I --> J[Slack - Alert Collateral Team]
    E --> K[PostgreSQL - Store Risk Metrics]
    E --> L[Code Node - Generate Risk Dashboard]
    L --> M[Email - Risk Dashboard]
    K --> M
```

## Description
This diagram illustrates the Counterparty Risk Monitor workflow that tracks and analyzes counterparty credit risk across the portfolio.

## Key Components
- **Scheduled Execution**: Runs hourly
- **Data Integration**: Collects counterparty and exposure data
- **Risk Calculation**: Computes credit risk metrics
- **Threshold Monitoring**: Identifies high-risk counterparties
- **Collateral Management**: Initiates margin calls when needed
- **Team Notification**: Alerts relevant teams of risk events
- **Reporting**: Generates comprehensive risk dashboards
