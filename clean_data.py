import os
import pandas as pd
import numpy as np

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

print("=" * 60)
print("BLUESTOCK DAY 2 - DATA CLEANING")
print("=" * 60)


def save(df, filename):
    path = os.path.join(PROCESSED_DIR, filename)
    df.to_csv(path, index=False)
    print(f"✔ Saved: {filename} | Rows: {len(df)}")


# ============================================================
# 01 FUND MASTER
# ============================================================

print("\nCleaning 01_fund_master.csv")

fund = pd.read_csv(os.path.join(RAW_DIR, "01_fund_master.csv"))

fund = fund.drop_duplicates()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund["expense_ratio_pct"] = pd.to_numeric(
    fund["expense_ratio_pct"],
    errors="coerce"
)

fund["exit_load_pct"] = pd.to_numeric(
    fund["exit_load_pct"],
    errors="coerce"
)

save(
    fund,
    "01_fund_master_cleaned.csv"
)

# ============================================================
# 02 NAV HISTORY
# ============================================================

print("\nCleaning 02_nav_history.csv")

nav = pd.read_csv(
    os.path.join(RAW_DIR, "02_nav_history.csv")
)

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav["nav"] = pd.to_numeric(
    nav["nav"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav.drop_duplicates()

nav = nav[
    nav["nav"] > 0
]

save(
    nav,
    "02_nav_history_cleaned.csv"
)

# ============================================================
# 03 AUM
# ============================================================

print("\nCleaning 03_aum_by_fund_house.csv")

aum = pd.read_csv(
    os.path.join(RAW_DIR, "03_aum_by_fund_house.csv")
)

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

for col in [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]:
    aum[col] = pd.to_numeric(
        aum[col],
        errors="coerce"
    )

aum = aum.drop_duplicates()

save(
    aum,
    "03_aum_by_fund_house_cleaned.csv"
)

# ============================================================
# 04 MONTHLY SIP INFLOWS
# ============================================================

print("\nCleaning 04_monthly_sip_inflows.csv")

sip = pd.read_csv(
    os.path.join(RAW_DIR, "04_monthly_sip_inflows.csv")
)

sip = sip.drop_duplicates()

for col in [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]:
    sip[col] = pd.to_numeric(
        sip[col],
        errors="coerce"
    )

save(
    sip,
    "04_monthly_sip_inflows_cleaned.csv"
)

# ============================================================
# 05 CATEGORY INFLOWS
# ============================================================

print("\nCleaning 05_category_inflows.csv")

category = pd.read_csv(
    os.path.join(RAW_DIR, "05_category_inflows.csv")
)

category = category.drop_duplicates()

category["net_inflow_crore"] = pd.to_numeric(
    category["net_inflow_crore"],
    errors="coerce"
)

save(
    category,
    "05_category_inflows_cleaned.csv"
)

# ============================================================
# 06 INDUSTRY FOLIO COUNT
# ============================================================

print("\nCleaning 06_industry_folio_count.csv")

folio = pd.read_csv(
    os.path.join(RAW_DIR, "06_industry_folio_count.csv")
)

folio = folio.drop_duplicates()

for col in [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]:
    folio[col] = pd.to_numeric(
        folio[col],
        errors="coerce"
    )

save(
    folio,
    "06_industry_folio_count_cleaned.csv"
)

# ============================================================
# 07 SCHEME PERFORMANCE
# ============================================================

print("\nCleaning 07_scheme_performance.csv")

performance = pd.read_csv(
    os.path.join(RAW_DIR, "07_scheme_performance.csv")
)

performance = performance.drop_duplicates()

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

save(
    performance,
    "07_scheme_performance_cleaned.csv"
)

# ============================================================
# 08 INVESTOR TRANSACTIONS
# ============================================================

print("\nCleaning 08_investor_transactions.csv")

transactions = pd.read_csv(
    os.path.join(RAW_DIR, "08_investor_transactions.csv")
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

transactions["amount_inr"] = pd.to_numeric(
    transactions["amount_inr"],
    errors="coerce"
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.title()
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

transactions = transactions.drop_duplicates()

save(
    transactions,
    "08_investor_transactions_cleaned.csv"
)

# ============================================================
# 09 PORTFOLIO HOLDINGS
# ============================================================

print("\nCleaning 09_portfolio_holdings.csv")

portfolio = pd.read_csv(
    os.path.join(RAW_DIR, "09_portfolio_holdings.csv")
)

portfolio["weight_pct"] = pd.to_numeric(
    portfolio["weight_pct"],
    errors="coerce"
)

portfolio["market_value_cr"] = pd.to_numeric(
    portfolio["market_value_cr"],
    errors="coerce"
)

portfolio["current_price_inr"] = pd.to_numeric(
    portfolio["current_price_inr"],
    errors="coerce"
)

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

portfolio = portfolio.drop_duplicates()

save(
    portfolio,
    "09_portfolio_holdings_cleaned.csv"
)

# ============================================================
# 10 BENCHMARK INDICES
# ============================================================

print("\nCleaning 10_benchmark_indices.csv")

benchmark = pd.read_csv(
    os.path.join(RAW_DIR, "10_benchmark_indices.csv")
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

benchmark["close_value"] = pd.to_numeric(
    benchmark["close_value"],
    errors="coerce"
)

benchmark = benchmark.drop_duplicates()

save(
    benchmark,
    "10_benchmark_indices_cleaned.csv"
)

print("\n" + "=" * 60)
print("ALL 10 DATASETS CLEANED SUCCESSFULLY")
print("=" * 60)