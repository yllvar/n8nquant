# Liquidity Risk Dashboard - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - 1 min] --> B[PostgreSQL - Fetch Liquidity Data]
    B --> C[Code Node - Calculate Metrics]
    C --> D{Check Critical Liquidity}
    D -->|Critical| E[Slack - Send Alert]
    D -->|Normal| F[PostgreSQL - Store Metrics]
    C --> F
    F --> G[Code Node - Portfolio Liquidity]
    G --> H[Email - Liquidity Dashboard]
```

## Description
This diagram illustrates the Liquidity Risk Dashboard workflow that monitors and analyzes portfolio liquidity metrics in real-time.

## Key Components
- **High-Frequency Updates**: Runs every minute
- **Liquidity Metrics**: Calculates key liquidity indicators
- **Threshold Monitoring**: Identifies critical liquidity conditions
- **Alerting**: Notifies risk teams of liquidity concerns
- **Data Storage**: Maintains historical liquidity metrics
- **Visualization**: Generates comprehensive liquidity dashboards
