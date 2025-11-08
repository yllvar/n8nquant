# FX Exposure Hedger - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - 15 min] --> B[PostgreSQL - Fetch FX Exposures]
    A --> C[HTTP Request - FX Rates API]
    B --> D[Code Node - Calculate Hedge Orders]
    C --> D
    D --> E{Check Hedge Threshold}
    D --> F[Code Node - Calculate Effectiveness]
    E -->|Hedge Needed| G[HTTP Request - Trading API]
    E -->|No Hedge| H[Email - Monitoring Update]
    G --> I[PostgreSQL - Store Hedge Order]
    G --> J[Slack - Alert Treasury Team]
    F --> K[Email - Effectiveness Report]
```

## Description
This diagram illustrates the FX Exposure Hedger workflow that monitors and manages foreign exchange risk through automated hedging strategies.

## Key Components
- **Scheduled Execution**: Runs every 15 minutes
- **Exposure Analysis**: Calculates net FX exposures
- **Threshold Monitoring**: Identifies when hedging is required
- **Order Generation**: Creates appropriate hedge orders
- **Effectiveness Tracking**: Measures hedge performance
- **Team Notification**: Alerts treasury team of actions taken
