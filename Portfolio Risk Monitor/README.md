# Portfolio Risk Monitor - VaR Calculator

## Overview
Real-time Value at Risk (VaR) calculation using historical simulation with automated breach detection and risk team alerts.

## Workflow Description
Calculates 95% VaR using historical simulation method, monitors for risk limit breaches, and provides daily risk reporting to portfolio managers and risk teams.

## Implementation Guide

### 1. Prerequisites
- Portfolio positions database
- Historical price data (1+ years)
- VaR limits configured per portfolio
- Slack/Email for alerts

### 2. Database Setup
Create `portfolio_positions`, `risk_calculations`, and `risk_limits` tables.

### 3. n8n Configuration Steps
- Import workflow and configure database connections
- Set up alert channels
- Configure risk parameters

### 4. VaR Methodology
- **Method**: Historical Simulation
- **Confidence**: 95%
- **Lookback**: 252 trading days

### 5. Testing
Test with sample portfolio data and verify breach scenarios.

### 6. Monitoring
Daily review of VaR calculations and monthly backtesting.