# Performance Attribution System - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - EOD] --> B[PostgreSQL - Fetch Portfolio Positions]
    A --> C[PostgreSQL - Fetch Daily Returns]
    A --> D[PostgreSQL - Fetch Factor Returns]
    B --> E[Code Node - Calculate Attribution]
    C --> E
    D --> E
    E --> F{Check Significant Active Returns}
    E --> G[PostgreSQL - Store Attribution Results]
    F -->|Significant| H[Slack - Alert Performance Moves]
    E --> I[Code Node - Generate Attribution Report]
    I --> J[Email - Attribution Report]
    G --> J
```

## Description
This diagram illustrates the Performance Attribution System workflow that analyzes and attributes portfolio performance to various factors and investment decisions.

## Key Components
- **Scheduled Execution**: Runs at end of day
- **Data Integration**: Collects portfolio, returns, and factor data
- **Attribution Analysis**: Attributes performance to factors and decisions
- **Anomaly Detection**: Identifies significant performance impacts
- **Result Storage**: Maintains historical attribution data
- **Reporting**: Generates detailed performance reports
- **Team Notification**: Alerts on significant performance moves
