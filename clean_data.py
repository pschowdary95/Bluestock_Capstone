import pandas as pd

# NAV HISTORY
nav = pd.read_csv("data/raw/nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

# TRANSACTIONS
txn = pd.read_csv(
    "data/raw/investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.upper()
)

txn = txn[txn["amount"] > 0]

txn.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

# PERFORMANCE
perf = pd.read_csv(
    "data/raw/scheme_performance.csv"
)

perf["expense_ratio"] = pd.to_numeric(
    perf["expense_ratio"]
)

perf = perf[
    (perf["expense_ratio"] >= 0.1)
    &
    (perf["expense_ratio"] <= 2.5)
]

perf.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Data Cleaning Complete")