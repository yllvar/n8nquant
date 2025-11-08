# Automated Portfolio Reconciliation Engine

## Overview
Automates daily portfolio reconciliation between internal systems and prime brokers with break detection and resolution workflows.

## Workflow Description
Fetches internal and prime broker positions, reconciles differences, identifies breaks, auto-resolves simple breaks, and escalates complex issues.

## Implementation Guide

### 1. Prerequisites
- Internal position data
- Prime broker API
- Break detection logic
- Operations notifications

### 2. Database Setup
Create `reconciliation_breaks` and `portfolio_positions` tables.

### 3. n8n Configuration Steps
- Import workflow and configure data sources
- Set up reconciliation logic
- Configure break resolution

### 4. Testing
Test with sample positions and verify break detection.

### 5. Monitoring
Monitor reconciliation accuracy and break resolution.

### 6. Troubleshooting
Check for data synchronization and reconciliation logic errors.