# Regulatory Reporting Automation - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - EOD] --> B[PostgreSQL - Fetch Daily Trades]
    B --> C{Validate Trade Data}
    C -->|Valid| D[Code Node - Format XML Report]
    C -->|Invalid| E[Set Node - Log Validation Error]
    D --> F[HTTP Request - Submit to API]
    E --> G[Slack - Alert Compliance Team]
    F --> H[PostgreSQL - Update Status]
    H --> I[Email - Compliance Summary]
    G --> I
```

## Description
This diagram shows the Regulatory Reporting Automation workflow that processes and submits daily trade reports to regulatory bodies.

## Key Components
- **Scheduled Execution**: Runs at end of day
- **Data Validation**: Ensures trade data compliance
- **Report Generation**: Formats data for regulatory submission
- **API Integration**: Submits reports to regulatory API
- **Status Tracking**: Updates submission status
- **Alerting**: Notifies team of validation issues
