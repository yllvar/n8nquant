# Factor Model Data Aggregator - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - Daily] --> B[PostgreSQL - Fetch Universe Symbols]
    B --> C[HTTP Request - Fundamental Data API]
    B --> D[PostgreSQL - Fetch Price Data]
    A --> E[HTTP Request - Macro Data API]
    C --> F[Code Node - Calculate Factor Exposures]
    D --> F
    E --> F
    F --> G[PostgreSQL - Store Factor Data]
    F --> H[Code Node - Generate Analytics]
    H --> I[Email - Factor Update Report]
```

## Description
This diagram shows the Factor Model Data Aggregator workflow that collects, processes, and analyzes factor model data for quantitative research and portfolio construction.

## Key Components
- **Scheduled Execution**: Runs daily
- **Data Collection**: Gathers fundamental and macroeconomic data
- **Factor Calculation**: Computes factor exposures
- **Data Storage**: Maintains historical factor data
- **Analytics**: Generates insights and metrics
- **Reporting**: Distributes factor analysis
