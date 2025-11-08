# Corporate Actions Processor - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - 3x Daily] --> B[HTTP Request - Corporate Actions API]
    A --> C[PostgreSQL - Fetch Portfolio Symbols]
    B --> D[Code Node - Filter Relevant Actions]
    C --> D
    D --> E{Check Dividend Actions}
    D --> F{Check Stock Split Actions}
    E -->|Yes| G[Code Node - Process Dividends]
    F -->|Yes| H[Code Node - Process Splits]
    G --> I[PostgreSQL - Store Dividend Payments]
    H --> J[PostgreSQL - Adjust Positions]
    D --> K[Slack - New Actions Alert]
    I --> L[Code Node - Generate Summary]
    J --> L
    L --> M[Email - Corporate Actions Summary]
```

## Description
This diagram illustrates the Corporate Actions Processor workflow that automates the processing of corporate actions and their impact on investment portfolios.

## Key Components
- **Scheduled Execution**: Runs three times daily
- **Data Integration**: Fetches corporate actions from API
- **Portfolio Impact**: Identifies affected positions
- **Action Processing**: Handles dividends and stock splits
- **Position Management**: Updates portfolio records
- **Notification**: Alerts team of new actions
- **Reporting**: Summarizes processed actions
