# Real-Time Liquidity Risk Dashboard

## Overview
Monitors real-time liquidity metrics, bid-ask spreads, and market depth with alerts for deteriorating liquidity conditions.

## Workflow Description
Calculates liquidity risk metrics every minute, monitors critical conditions, stores historical data, and alerts risk teams on liquidity deterioration.

## Implementation Guide

### 1. Prerequisites
- Real-time market data
- Portfolio position data
- Liquidity metrics calculation
- Risk team alerts

### 2. Database Setup
Create `liquidity_monitoring` and `market_data_real_time` tables.

### 3. n8n Configuration Steps
- Import workflow and configure data sources
- Set up liquidity scoring parameters
- Configure risk alerts

### 4. Testing
Verify liquidity calculations and alert thresholds.

### 5. Monitoring
Continuous monitoring of liquidity scores and market conditions.

### 6. Troubleshooting
Check for data freshness and calculation accuracy.