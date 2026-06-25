# Bluestock Mutual Fund Analytics - Data Dictionary

## 1. 01_fund_master.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | TEXT | Unique AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund Company |
| scheme_name | TEXT | Scheme Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub Category |
| plan | TEXT | Direct / Regular |
| launch_date | DATE | Launch Date |
| benchmark | TEXT | Benchmark Index |
| expense_ratio_pct | REAL | Expense Ratio (%) |
| exit_load_pct | REAL | Exit Load (%) |
| min_sip_amount | REAL | Minimum SIP Amount |
| min_lumpsum_amount | REAL | Minimum Lump Sum |
| fund_manager | TEXT | Fund Manager |
| risk_category | TEXT | Risk Category |
| sebi_category_code | TEXT | SEBI Category Code |

---

## 2. 02_nav_history.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | TEXT | Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## 3. 03_aum_by_fund_house.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | AUM Date |
| fund_house | TEXT | Fund House |
| aum_lakh_crore | REAL | AUM (Lakh Crore) |
| aum_crore | REAL | AUM (Crore) |
| num_schemes | INTEGER | Number of Schemes |

---

## 4. 04_monthly_sip_inflows.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | TEXT | Month |
| sip_inflow_crore | REAL | SIP Inflow |
| active_sip_accounts_crore | REAL | Active SIP Accounts |
| new_sip_accounts_lakh | REAL | New SIP Accounts |
| sip_aum_lakh_crore | REAL | SIP AUM |
| yoy_growth_pct | REAL | Year-on-Year Growth |

---

## 5. 05_category_inflows.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | TEXT | Month |
| category | TEXT | Fund Category |
| net_inflow_crore | REAL | Net Inflow |

---

## 6. 06_industry_folio_count.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | TEXT | Month |
| total_folios_crore | REAL | Total Folios |
| equity_folios_crore | REAL | Equity Folios |
| debt_folios_crore | REAL | Debt Folios |
| hybrid_folios_crore | REAL | Hybrid Folios |
| others_folios_crore | REAL | Other Folios |

---

## 7. 07_scheme_performance.csv

Contains:
- Returns (1 Year, 3 Year, 5 Year)
- Alpha
- Beta
- Sharpe Ratio
- Sortino Ratio
- Standard Deviation
- Maximum Drawdown
- AUM
- Expense Ratio
- Morningstar Rating
- Risk Grade

---

## 8. 08_investor_transactions.csv

Contains:
- Investor ID
- Transaction Date
- AMFI Code
- Transaction Type
- Amount
- State
- City
- City Tier
- Age Group
- Gender
- Annual Income
- Payment Mode
- KYC Status

---

## 9. 09_portfolio_holdings.csv

Contains:
- Stock Symbol
- Stock Name
- Sector
- Weight %
- Market Value
- Current Price
- Portfolio Date

---

## 10. 10_benchmark_indices.csv

Contains:
- Date
- Index Name
- Closing Value

---

## Data Source

- AMFI India
- mfapi.in
- NSE India
- BSE India

Project: Bluestock Mutual Fund Analytics Capstone