# Data Dictionary

## nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

## investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor Identifier |
| amfi_code | Integer | Fund Code |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount | Float | Investment Amount |
| kyc_status | Text | KYC Verification Status |
| state | Text | Investor State |

## scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund Code |
| fund_name | Text | Mutual Fund Name |
| return_1y | Float | 1 Year Return |
| return_3y | Float | 3 Year Return |
| return_5y | Float | 5 Year Return |
| expense_ratio | Float | Fund Expense Ratio |
| aum | Float | Assets Under Management |