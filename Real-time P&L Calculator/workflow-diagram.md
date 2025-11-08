# Real-time P&L Calculator - Workflow Diagram

```mermaid
graph TD
    A[Webhook - Price Update] --> B[PostgreSQL - Fetch Positions]
    B --> C[Code Node - Calculate P&L]
    C --> D[PostgreSQL - Store P&L Data]
    C --> E{Check P&L Threshold}
    E -->|Large Movement| F[Slack - P&L Alert]
    E -->|Normal Movement| G[Redis - Publish Update]
    D --> G
    D --> H[Code Node - Aggregate Portfolio P&L]
    H --> I[Email - P&L Summary]
```

## Description
This diagram illustrates the Real-time P&L Calculator workflow that processes price updates to calculate and track portfolio performance.

## Key Components
- **Event-Driven**: Triggered by price updates
- **Position Management**: Fetches current portfolio positions
- **P&L Calculation**: Computes profit/loss in real-time
- **Threshold Monitoring**: Alerts on significant P&L movements
- **Data Persistence**: Stores P&L history
- **Real-time Updates**: Publishes updates via Redis
- **Reporting**: Generates summary reports
