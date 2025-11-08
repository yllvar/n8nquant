# Research Data Pipeline - Workflow Diagram

```mermaid
graph TD
    A[Cron Trigger - 30 min] --> B[HTTP Request - News API]
    A --> C[HTTP Request - Social Sentiment API]
    A --> D[HTTP Request - Earnings Transcripts API]
    B --> E[Code Node - Analyze News Sentiment]
    C --> F[Code Node - Process Social Sentiment]
    D --> G[Code Node - Analyze Earnings Transcripts]
    E --> H[Code Node - Aggregate Research Data]
    F --> H
    G --> H
    H --> I[PostgreSQL - Store Research Data]
    H --> J[Code Node - Generate Research Insights]
    J --> K[Slack - Research Insights Update]
    J --> L[Email - Research Insights Report]
```

## Description
This diagram shows the Research Data Pipeline workflow that collects, processes, and analyzes alternative data sources for quantitative research.

## Key Components
- **Scheduled Execution**: Runs every 30 minutes
- **Data Collection**: Gathers data from multiple sources
- **Sentiment Analysis**: Processes textual data for market sentiment
- **Data Aggregation**: Combines multiple data streams
- **Insight Generation**: Identifies actionable research signals
- **Distribution**: Delivers insights to research teams
