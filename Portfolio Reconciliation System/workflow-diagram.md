# Portfolio Reconciliation System - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - EOD] --> B[PostgreSQL - Internal Positions]
    A --> C[HTTP Request - Prime Broker API]
    B --> D[Code Node - Reconcile Positions]
    C --> D
    D --> E{Check Critical Breaks}
    D --> F[PostgreSQL - Store Reconciliation Breaks]
    E -->|Critical| G[Slack - Alert Ops Team]
    D --> H[Code Node - Auto-Resolve Breaks]
    H --> I[PostgreSQL - Update Resolved]
    H --> J[Email - Reconciliation Report]
    F --> J
```

## Description
This diagram illustrates the Portfolio Reconciliation System workflow that ensures consistency between internal records and prime broker statements, identifying and resolving any discrepancies.

## Key Components
- **Scheduled Execution**: Runs at end of day
- **Data Integration**: Fetches positions from internal and external sources
- **Reconciliation Engine**: Compares and matches positions
- **Break Resolution**: Implements automated resolution rules
- **Exception Handling**: Manages critical breaks requiring manual intervention
- **Audit Trail**: Maintains reconciliation history
- **Reporting**: Generates reconciliation reports for compliance
