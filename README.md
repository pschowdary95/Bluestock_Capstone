# 📊 Bluestock Mutual Fund Analytics
<<<<<<< HEAD
A complete end-to-end Data Analytics Capstone Project that analyzes Indian Mutual Fund data using Python, SQLite, Power BI, and Data Visualization techniques. The project focuses on transforming raw financial datasets into meaningful insights through ETL, Exploratory Data Analysis (EDA), Performance Analytics, Risk Analysis, and Interactive Dashboards.
---
# 📌 Project Overview
The Mutual Fund Analytics project is designed to help investors and financial analysts understand mutual fund performance using historical NAV data, SIP inflows, AUM, benchmark indices, and portfolio holdings.
The project integrates multiple datasets, performs data cleaning, calculates financial metrics, stores processed data in SQLite, and visualizes insights using Power BI.
---

# 🎯 Problem Statement
Mutual fund investors often struggle to compare funds because the required information is spread across multiple datasets and reports.
This project aims to:
=======

A complete end-to-end Data Analytics Capstone Project that analyzes Indian Mutual Fund data using Python, SQLite, Power BI, and Data Visualization techniques. The project focuses on transforming raw financial datasets into meaningful insights through ETL, Exploratory Data Analysis (EDA), Performance Analytics, Risk Analysis, and Interactive Dashboards.

---

# 📌 Project Overview

The Mutual Fund Analytics project is designed to help investors and financial analysts understand mutual fund performance using historical NAV data, SIP inflows, AUM, benchmark indices, and portfolio holdings.

The project integrates multiple datasets, performs data cleaning, calculates financial metrics, stores processed data in SQLite, and visualizes insights using Power BI.

---

# 🎯 Problem Statement

Mutual fund investors often struggle to compare funds because the required information is spread across multiple datasets and reports.

This project aims to:

>>>>>>> ac635b1 (Added professional README)
- Integrate multiple mutual fund datasets
- Build an automated ETL pipeline
- Perform financial performance analysis
- Calculate investment risk metrics
- Generate business insights
- Recommend suitable funds based on risk category
- Build an interactive Power BI dashboard for visualization

---

# 🏗 Project Architecture

```
Raw CSV Files
        │
        ▼
 Data Cleaning (Python)
        │
        ▼
 Data Transformation
        │
        ▼
 SQLite Database
        │
        ▼
EDA & Performance Analytics
        │
        ▼
Advanced Analytics
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights & Recommendations
```

---

# 📂 Folder Structure

```
Bluestock_Capstone/

│
├── data/
│   ├── raw/
│   ├── processed/
│
├── database/
│   └── bluestock_mf.db
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── charts/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── recommender.py
├── clean_data.py
├── load_db.py
├── schema.sql
├── queries.sql
├── requirements.txt
├── bluestock_mf_dashboard.pbix
└── README.md
```

---

# 📁 Dataset Description

The project uses ten official mutual fund datasets.

| Dataset | Description |
|----------|-------------|
| Fund Master | Details of mutual fund schemes |
| NAV History | Historical NAV values |
| AUM by Fund House | Assets Under Management |
| Monthly SIP Inflows | Monthly SIP investments |
| Category Inflows | Category-wise inflows |
| Industry Folio Count | Investor folio statistics |
| Scheme Performance | Fund performance metrics |
| Investor Transactions | Purchase and redemption details |
| Portfolio Holdings | Top holdings of funds |
| Benchmark Indices | Market benchmark performance |

Total Records: **1.3+ Million**

---

# 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- SQLite
- SQL
- Power BI
- Jupyter Notebook
- Git & GitHub

---

# 🔄 ETL Pipeline

The ETL pipeline performs the following tasks:

### Extract

- Reads multiple CSV files
- Loads historical financial datasets

### Transform

- Removes duplicate records
- Handles missing values
- Standardizes column names
- Converts data types
- Cleans invalid records

### Load

- Loads processed data into SQLite database
- Creates Star Schema tables
- Enables SQL queries for analytics

---

# 🗄 SQLite Database

The project stores cleaned data inside a SQLite database.

Major tables include:

- fact_nav
- fact_aum
- fact_transactions
- fact_performance
- fact_portfolio
- fact_benchmark

Dimension tables:

- dim_fund
- dim_date
- dim_category

Benefits:

- Faster querying
- Structured storage
- Easy integration with analytics tools

---

# 📈 Exploratory Data Analysis (EDA)

EDA helps understand trends and patterns within mutual fund data.

Key analyses include:

- Daily NAV Trends
- Monthly SIP Growth
- AUM Distribution
- Fund Category Distribution
- Sector Allocation
- Expense Ratio Analysis
- Risk Category Distribution
- Correlation Analysis

Several visualizations were created using Matplotlib and Plotly.

---

# 📊 Performance Analytics

Performance metrics were calculated to evaluate mutual fund performance.

Metrics include:

- CAGR (Compound Annual Growth Rate)
- Alpha
- Beta
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Tracking Error

These metrics help compare funds based on return and risk.

---

# 🤖 Advanced Analytics

Advanced financial analysis includes:

- Rolling Sharpe Ratio
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Herfindahl-Hirschman Index (HHI)
- Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation Engine

The recommendation system suggests top-performing funds based on risk category.

---

# 📊 Power BI Dashboard

A fully interactive dashboard was created using Power BI.

Dashboard includes:

- Total AUM
- Total Schemes
- Average CAGR
- Average Sharpe Ratio
- NAV Trend
- SIP Trend
- Top Performing Funds
- Risk Category Distribution
- Return vs Risk Analysis

Interactive slicers allow dynamic filtering by category and fund.

---

# 💡 Business Insights

The analysis revealed several important insights.

- Large-cap funds provide relatively stable returns.
- Small-cap funds generate higher returns with increased risk.
- SIP inflows have steadily increased over recent years.
- Diversified portfolios reduce investment risk.
- Sharpe Ratio effectively identifies better risk-adjusted funds.
- Risk-based recommendations help investors choose appropriate funds.

---

# ▶ How to Run

Clone the repository.

```bash
git clone https://github.com/pschowdary95/Bluestock_Capstone.git
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run data cleaning.

```bash
python clean_data.py
```

Load SQLite database.

```bash
python load_db.py
```

Run recommendation engine.

```bash
python recommender.py
```

Open:

- Performance_Analytics.ipynb
- Advanced_Analytics.ipynb

Finally open

```
bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

# 📌 Project Outputs

The project successfully delivers:

- Automated ETL pipeline
- SQLite Data Warehouse
- Comprehensive EDA
- Performance Analytics
- Advanced Risk Analytics
- Mutual Fund Recommendation Engine
- Interactive Power BI Dashboard
- Final Project Report
- Presentation Slides

---

# 🚀 Future Scope

Future improvements include:

- Live NAV updates using MFAPI
- Automated ETL Scheduling
- Streamlit Web Application
- Monte Carlo Portfolio Simulation
- Markowitz Portfolio Optimization
- AI-based Investment Recommendation
- Email Report Automation
- Cloud Deployment using AWS

---

# 👨‍💻 Author

**P. Subrahmanyam Chowdary**

B.Tech – Artificial Intelligence & Machine Learning

Sri Vasavi Engineering College

GitHub: https://github.com/pschowdary95

---
