# Margin Call Processing Automation

## Overview
Automates margin call processing, liquidation prioritization, and collateral management with treasury team notifications.

## Workflow Description
Monitors margin requirements from prime brokers, calculates available liquidity, auto-liquidates positions if needed, and notifies treasury team.

## Implementation Guide

### 1. Prerequisites
- Margin data
- Account balances
- Trading API
- Liquidation logic

### 2. Database Setup
Create `accounts` and `margin_call_logs` tables.

### 3. n8n Configuration Steps
- Import workflow and configure data sources
- Set up liquidation calculations
- Configure notifications

### 4. Testing
Test with margin call scenarios and verify liquidation logic.

### 5. Monitoring
Monitor margin call processing and liquidation success.

### 6. Troubleshooting
Check for balance data accuracy and execution errors.