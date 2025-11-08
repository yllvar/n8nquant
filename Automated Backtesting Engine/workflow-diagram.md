# Automated Backtesting Engine - Workflow Diagram

```mermaid
graph TD
    A[Manual Trigger] --> B[Code Node - Load Strategy Config]
    B --> C[PostgreSQL - Fetch Historical Data]
    C --> D[Code Node - Execute Backtest]
    D --> E[Code Node - Calculate Performance]
    E --> F[PostgreSQL - Store Results]
    E --> G[Email - Send Report]
    F --> G
```

## Description
This diagram illustrates the Automated Backtesting Engine workflow that executes trading strategy backtests and generates performance reports.

## Key Components
- **Manual Trigger**: Initiated on demand
- **Strategy Configuration**: Loads specific strategy parameters
- **Historical Data**: Retrieves relevant market data
- **Backtest Execution**: Runs the strategy simulation
- **Performance Analysis**: Calculates key metrics
- **Reporting**: Stores results and sends email reports
