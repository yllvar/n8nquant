# Stress Testing Framework - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - Overnight] --> B[PostgreSQL - Fetch Portfolio Positions]
    A --> C[Code Node - Load Stress Scenarios]
    B --> D[Code Node - Apply Stress Scenarios]
    C --> D
    D --> E{Check Regulatory Breaches}
    D --> F[PostgreSQL - Store Stress Results]
    E -->|Breach| G[Slack - Alert Risk Team]
    D --> H[Code Node - Generate Stress Report]
    H --> I[Email - Stress Testing Report]
    F --> I
```

## Description
This diagram shows the Stress Testing Framework workflow that applies various stress scenarios to assess portfolio resilience under adverse market conditions.

## Key Components
- **Scheduled Execution**: Runs overnight
- **Scenario Management**: Applies predefined stress scenarios
- **Portfolio Analysis**: Evaluates impact on portfolio positions
- **Regulatory Compliance**: Checks against risk limits
- **Result Storage**: Maintains historical stress test results
- **Reporting**: Generates comprehensive stress test reports
