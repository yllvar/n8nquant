# Real-Time Market Data Pipeline

## Overview
Automated ETL pipeline for real-time market data collection, validation, and storage with comprehensive monitoring and alerting.

## Workflow Description
This workflow fetches real-time market data from financial APIs every 5 minutes, validates data quality, stores it in PostgreSQL, and generates performance metrics with automated alerting for data issues.

## Implementation Guide

### 1. Prerequisites
- n8n instance (v1.0+)
- PostgreSQL database
- Market data API access
- Slack webhook for alerts

### 2. Database Setup
Create `market_data_real_time` and `pipeline_metrics` tables with appropriate indexes.

### 3. n8n Configuration Steps
- Import the workflow JSON file
- Configure PostgreSQL and HTTP credentials
- Set API keys and endpoints
- Customize validation thresholds

### 4. Environment Variables
Set `MARKET_DATA_API_URL`, `MARKET_DATA_API_KEY`, `DB_HOST`, and `SLACK_WEBHOOK_URL`.

### 5. Testing
Execute manually to verify API connectivity, data validation, and alerting functionality.

### 6. Monitoring
Regularly check execution logs, database storage, and API usage.

### 7. Troubleshooting
Common issues include API rate limits, database connection failures, and data validation errors.
