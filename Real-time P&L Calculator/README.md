# Real-time P&L Calculation Engine

## Overview
Real-time P&L calculation engine that processes market price updates and calculates position valuations with portfolio aggregation.

## Workflow Description
Streams trade and position data, calculates unrealized P&L using live market prices, aggregates P&L across portfolios, and feeds to trading desks.

## Implementation Guide

### 1. Prerequisites
- Position data
- Market prices
- P&L calculations
- Portfolio aggregation

### 2. Database Setup
Create `pnl_calculations` and `positions` tables.

### 3. n8n Configuration Steps
- Import workflow and configure data sources
- Set up P&L calculations
- Configure aggregation logic

### 4. Testing
Test with sample positions and verify P&L calculations.

### 5. Monitoring
Monitor calculation accuracy and data freshness.

### 6. Troubleshooting
Check for data synchronization and calculation errors.