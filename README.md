# Quantitative Finance n8nQuant Workflows

A collection of production-ready n8nQuant workflows specifically designed for quantitative finance applications. Each workflow is fully documented, tested, and includes comprehensive error handling, monitoring, and integration capabilities.

## 📋 Workflow Catalog

| # | Workflow Name | Category | Description | Directory |
|---|---------------|----------|-------------|-----------|

## 🚀 Quick Start Guide

### Prerequisites

- n8n instance (v1.0+ recommended)
- PostgreSQL database
- Access to financial data APIs
- Notification services (Slack/Email) for alerts

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <n8nQuant>
   cd n8nQuant
   ```

2. **Environment Configuration:**
   Create a `.env` file in the root directory with your configuration:
   ```env
   # Database
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=quant_finance
   DB_USER=your_username
   DB_PASSWORD=your_password

   # APIs
   MARKET_DATA_API_URL=https://api.marketdata.com  
   MARKET_DATA_API_KEY=your_api_key
   SLACK_WEBHOOK_URL=https://hooks.slack.com/your-webhook  

   # Email
   SMTP_HOST=smtp.yourcompany.com
   SMTP_PORT=587
   SMTP_USER=your_email@company.com
   SMTP_PASSWORD=your_password
   ```

3. **Import workflows to n8n:**
   - Navigate to your n8n instance
   - Go to Settings > Workflows
   - Click "Import from file" for each workflow JSON
   - Configure credentials for each service

## 📊 Workflow Categories

### 📊 Data Management
- **Real-Time Market Data Pipeline** - ETL pipeline for processing and validating real-time market data feeds
- **Research Data Pipeline** - Aggregates and processes alternative data sources for quantitative research
- **Factor Model Data Aggregator** - Collects and processes factor model data for quantitative analysis

### ⚖️ Risk Management
- **Portfolio Risk Monitor** - Real-time VaR calculation with breach alerts
- **Liquidity Risk Dashboard** - Monitors liquidity metrics and generates alerts
- **Counterparty Risk Monitor** - Tracks and analyzes counterparty exposure
- **Margin Call Processor** - Automated processing of margin calls and collateral management
- **Stress Testing Framework** - Performs scenario analysis and stress testing

### 🔄 Trading & Execution
- **Algorithmic Trading Signal Generator** - Generates trading signals using quantitative models
- **Best Execution Monitor** - Trades execution quality and best execution compliance
- **FX Exposure Hedger** - Manages and hedges foreign exchange exposure

### 📈 Performance & Analytics
- **Real-time P&L Calculator** - Calculates and aggregates real-time profit and loss
- **Performance Attribution System** - Attributes performance to various risk factors
- **Portfolio Reconciliation System** - Reconciles positions and transactions across systems

### 🔧 Operations & Compliance
- **Corporate Actions Processor** - Automates corporate action processing
- **Regulatory Reporting Automation** - Generates and submits regulatory reports
- **Quant Strategy Deployment Pipeline** - CI/CD pipeline for quantitative strategies

### 📊 Market Data & Analytics
- **Corporate Bond Pricing Engine** - Real-time pricing for corporate bonds
- **Volatility Surface Builder** - Constructs and analyzes volatility surfaces
- **Automated Backtesting Engine** - Backtests trading strategies with historical data

## 📈 Workflow Details

### 1. Real-Time Market Data Pipeline
**File:** `real-time-market-data-pipeline/real-time-market-data-pipeline.json`

Fetches, validates, and stores real-time market data with comprehensive error handling and quality monitoring.

**Key Features:**
- 5-minute interval data collection
- Data validation and quality checks
- Error logging and alerting
- Performance metrics calculation

**Nodes Used:**
- Cron Trigger
- HTTP Request (Market Data API)
- If (Data Validation)
- PostgreSQL (Data Storage)
- Code (Metrics Calculation)
- Slack (Alerts)

### 2. Portfolio Risk Monitor
**File:** `portfolio-risk-monitor/portfolio-risk-monitor.json`

Calculates Value at Risk (VaR) using historical simulation and monitors for risk limit breaches.

**Key Features:**
- Historical simulation VaR (95% confidence)
- Real-time breach detection
- Multi-channel alerts
- Daily risk reporting

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Portfolio Data)
- Code (VaR Calculation)
- If (Breach Detection)
- Slack/Email (Alerts)

### 3. Automated Backtesting Engine
**File:** `automated-backtesting-engine/automated-backtesting-engine.json`

Comprehensive backtesting framework for quantitative strategies with performance analytics.

**Key Features:**
- Multiple strategy configurations
- Performance metrics (Sharpe, Max Drawdown)
- Walk-forward analysis
- Detailed reporting

**Nodes Used:**
- Manual Trigger
- PostgreSQL (Historical Data)
- Code (Backtest Engine)
- Email (Reports)

### 4. Regulatory Reporting Automation
**File:** `regulatory-reporting-automation/regulatory-reporting-automation.json`

Automates MiFID II transaction reporting with validation and compliance monitoring.

**Key Features:**
- Daily trade aggregation
- XML report generation
- Regulatory API submission
- Compliance status tracking

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Trade Data)
- Code (XML Generation)
- HTTP Request (Regulatory API)
- Email (Compliance Summary)

### 5. Real-Time Liquidity Risk Dashboard
**File:** `real-time-liquidity-risk-dashboard/real-time-liquidity-risk-dashboard.json`

Monitors real-time liquidity metrics and alerts on deteriorating market conditions.

**Key Features:**
- 1-minute monitoring intervals
- Bid-ask spread analysis
- Market depth monitoring
- Portfolio-level liquidity scoring

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Market Data)
- Code (Liquidity Metrics)
- If (Alert Conditions)
- Slack/Email (Alerts)

### 6. Volatility Surface Construction Engine
**File:** `volatility-surface-construction-engine/volatility-surface-construction-engine.json`

Builds and maintains real-time volatility surfaces for options pricing and risk management.

**Key Features:**
- SVI parameterization
- Arbitrage checks
- Surface quality monitoring
- Term structure analysis

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Options Data)
- Code (Surface Construction)
- If (Quality Checks)
- Email (Analysis Reports)

### 7. Corporate Actions Automation Engine
**File:** `corporate-actions-automation-engine/corporate-actions-automation-engine.json`

Automates processing of corporate actions including dividends, splits, and mergers.

**Key Features:**
- Multi-source action monitoring
- Position adjustment automation
- Cash reconciliation
- Operations team alerts

**Nodes Used:**
- Cron Trigger
- HTTP Request (Corporate Actions API)
- PostgreSQL (Portfolio Data)
- Code (Action Processing)
- Slack/Email (Notifications)

### 8. Quantitative Factor Model Data Pipeline
**File:** `quantitative-factor-model-data-pipeline/quantitative-factor-model-data-pipeline.json`

Aggregates and processes multi-source data for quantitative factor models.

**Key Features:**
- Fundamental data collection
- Macroeconomic indicator processing
- Factor exposure calculation
- Data quality assessment

**Nodes Used:**
- Cron Trigger
- HTTP Request (Data APIs)
- PostgreSQL (Storage)
- Code (Factor Calculation)
- Email (Data Updates)

### 9. Algorithmic Trading Signal Generation Engine
**File:** `algorithmic-trading-signal-generation-engine/algorithmic-trading-signal-generation-engine.json`

Generates real-time trading signals using multiple quantitative strategies.

**Key Features:**
- Multi-strategy signal generation
- Risk parameter validation
- Kafka integration for execution
- Real-time performance analytics

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Market Data)
- Code (Signal Generation)
- Kafka (Execution)
- Slack/Email (Alerts)

### 10. Automated Portfolio Reconciliation Engine
**File:** `automated-portfolio-reconciliation-engine/automated-portfolio-reconciliation-engine.json`

Automates daily portfolio reconciliation between internal systems and prime brokers.

**Key Features:**
- Break detection and classification
- Auto-resolution of simple breaks
- Operations team escalation
- Reconciliation reporting

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Internal Positions)
- HTTP Request (Prime Broker API)
- Code (Reconciliation Logic)
- Email (Summary Reports)

### 11. FX Exposure Hedging Automation
**File:** `fx-exposure-hedging-automation/fx-exposure-hedging-automation.json`

Monitors FX exposures and automatically executes hedging strategies.

**Key Features:**
- Real-time exposure monitoring
- Optimal hedge ratio calculation
- Automated order execution
- Hedge effectiveness reporting

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Portfolio Data)
- HTTP Request (FX Rates API)
- Code (Hedge Calculation)
- HTTP Request (Trading API)

### 12. Comprehensive Stress Testing Engine
**File:** `comprehensive-stress-testing-engine/comprehensive-stress-testing-engine.json`

Performs multi-scenario stress testing across portfolios with regulatory compliance.

**Key Features:**
- Historical and hypothetical scenarios
- Regulatory compliance checks
- Concentration risk analysis
- Executive reporting

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Portfolio Data)
- Code (Scenario Application)
- If (Regulatory Breaches)
- Email (Comprehensive Reports)

### 13. Counterparty Credit Risk Monitoring System
**File:** `counterparty-credit-risk-monitoring-system/counterparty-credit-risk-monitoring-system.json`

Monitors counterparty credit risk with CVA calculation and collateral management.

**Key Features:**
- Real-time credit rating monitoring
- CVA and expected loss calculation
- Collateral requirement analysis
- Margin call automation

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Counterparty Data)
- HTTP Request (Credit API)
- Code (Risk Metrics)
- HTTP Request (Collateral API)

### 14. Quantitative Research Data Pipeline
**File:** `quantitative-research-data-pipeline/quantitative-research-data-pipeline.json`

Aggregates alternative data sources for quantitative research and sentiment analysis.

**Key Features:**
- News sentiment analysis (NLP)
- Social media sentiment tracking
- Earnings call transcript processing
- Composite sentiment scoring

**Nodes Used:**
- Cron Trigger
- HTTP Request (Multiple APIs)
- Code (Sentiment Analysis)
- PostgreSQL (Research Data)
- Slack/Email (Insights)

### 15. Portfolio Performance Attribution Engine
**File:** `portfolio-performance-attribution-engine/portfolio-performance-attribution-engine.json`

Performs daily performance attribution using Brinson-Fachler models and factor analysis.

**Key Features:**
- Brinson-Fachler attribution
- Factor model integration
- Contribution analysis
- Attribution quality assessment

**Nodes Used:**
- Cron Trigger
- PostgreSQL (Portfolio Data)
- Code (Attribution Calculation)
- Email (Detailed Reports)

### 16. Margin Call Processing Automation
**File:** `margin-call-processing-automation/margin-call-processing-automation.json`

Automates margin call processing, liquidation prioritization, and collateral management.

**Key Features:**
- Real-time margin requirement monitoring
- Automated liquidation prioritization
- Collateral optimization
- Treasury team notifications

**Nodes Used:**
- Webhook Trigger (Margin Call Events)
- PostgreSQL (Account Data)
- Code (Liquidation Logic)
- HTTP Request (Trading API)
- Slack/Email (Notifications)

### 17. Best Execution Monitoring System
**File:** `best-execution-monitoring-system/best-execution-monitoring-system.json`

Monitors trade execution quality, calculates slippage, and ensures compliance with best execution obligations.

**Key Features:**
- Real-time execution quality scoring
- TCA (Transaction Cost Analysis)
- Benchmark comparison
- Compliance reporting

**Nodes Used:**
- Webhook Trigger (Trade Execution Events)
- PostgreSQL (Market Data)
- Code (Execution Quality Metrics)
- Email (Compliance Reports)

### 18. Corporate Bond Pricing Engine
**File:** `corporate-bond-pricing-engine/corporate-bond-pricing-engine.json`

Real-time corporate bond pricing engine with credit risk adjustment and liquidity factors.

**Key Features:**
- TRACE data integration
- Credit spread adjustment
- Liquidity factor incorporation
- Greeks calculation

**Nodes Used:**
- Cron Trigger
- HTTP Request (TRACE API)
- PostgreSQL (Bond Metadata)
- Code (Pricing Engine)
- Email (Pricing Reports)

### 19. Quant Strategy Deployment Pipeline
**File:** `quant-strategy-deployment-pipeline/quant-strategy-deployment-pipeline.json`

Automated CI/CD pipeline for quantitative strategies with testing, validation, and deployment.

**Key Features:**
- GitHub integration
- Automated testing (unit, integration)
- Backtest validation
- Docker deployment

**Nodes Used:**
- Webhook Trigger (GitHub Events)
- Execute Command (Tests)
- Execute Command (Docker Build)
- Redis (Deployment Queue)
- Slack (Deployment Notifications)

### 20. Real-time P&L Calculation Engine
**File:** `real-time-pnl-calculation-engine/real-time-pnl-calculation-engine.json`

Real-time P&L calculation engine that processes market price updates and calculates position valuations.

**Key Features:**
- Real-time P&L updates
- Portfolio aggregation
- Daily P&L calculation
- Large movement alerts

**Nodes Used:**
- Webhook Trigger (Price Updates)
- PostgreSQL (Position Data)
- Code (P&L Calculation)
- Redis (P&L Updates Queue)
- Slack/Email (Alerts)

## 🔧 Configuration

### Database Setup

Each workflow requires specific database tables. Refer to individual workflow documentation for table schemas and setup scripts.

### API Credentials

Configure the following API credentials in n8n:

- Market Data Providers (Bloomberg, Refinitiv, etc.)
- Credit Rating Agencies (Moody's, S&P, Fitch)
- Regulatory Reporting APIs
- Trading and Execution Platforms
- Communication Channels (Slack, Email)

### Monitoring and Alerting

Set up monitoring for:
- Workflow execution failures
- Data quality issues
- Risk limit breaches
- Regulatory compliance violations
- System performance metrics

## 📈 Production Considerations

### Error Handling
All workflows include comprehensive error handling with:
- Try-catch patterns
- Error logging to database
- Multi-channel alerting
- Retry mechanisms for transient failures

### Performance Optimization
- Database indexing for large datasets
- API rate limiting compliance
- Efficient data processing algorithms
- Memory management in code nodes

### Security
- API key management through n8n credentials
- Database connection security
- Data encryption at rest and in transit
- Access control for sensitive workflows

## 🛠️ Customization

Each workflow can be customized for:
- Different data sources
- Alternative calculation methodologies
- Custom alert thresholds
- Specific regulatory requirements
- Unique business logic

## 📞 Support

For workflow customization, implementation support, or questions:
1. Check individual workflow documentation
2. Review n8n node configuration guides
3. Consult the quantitative finance team for domain-specific questions

## 📄 License

This collection of workflows is provided for educational and professional use. Please ensure compliance with data provider licenses and regulatory requirements when deploying in production environments.

---
**Note:** If n8nQuant workflow saves you time and makes your quant development more efficient, please give a star on GitHub. It helps more developers discover this project!

**Note:** Always test workflows thoroughly in a development environment before deploying to production. Monitor performance and adjust configurations based on your specific requirements and data volumes.
