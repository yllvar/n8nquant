# Real-Time Market Data Pipeline - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - 5 min] --> B[HTTP Request - Market Data API]
    B --> C{Validate Market Data}
    C -->|Valid| D[PostgreSQL - Store Validated Data]
    C -->|Invalid| E[Set Node - Log Error]
    E --> F[Slack - Send Alert]
    D --> G[Code Node - Calculate Metrics]
    G --> H[PostgreSQL - Store Performance Metrics]
```

## Description
This diagram illustrates the Real-Time Market Data Pipeline workflow that runs every 5 minutes to fetch, validate, and store market data while calculating performance metrics.

## Key Components
- **Cron Trigger**: Scheduled to run every 5 minutes
- **Market Data API**: Fetches real-time market data
- **Data Validation**: Ensures data quality before storage
- **PostgreSQL**: Stores validated data and performance metrics
- **Alerting**: Sends notifications for data validation failures
