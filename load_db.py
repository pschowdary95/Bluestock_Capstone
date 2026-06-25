import os
import pandas as pd
from sqlalchemy import create_engine

PROCESSED_DIR = "data/processed"
DB_PATH = "database/bluestock_mf.db"

os.makedirs("database", exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}")

files = {
    "dim_fund": "01_fund_master_cleaned.csv",
    "fact_nav": "02_nav_history_cleaned.csv",
    "fact_aum": "03_aum_by_fund_house_cleaned.csv",
    "fact_sip_industry": "04_monthly_sip_inflows_cleaned.csv",
    "fact_category_inflows": "05_category_inflows_cleaned.csv",
    "fact_folio": "06_industry_folio_count_cleaned.csv",
    "fact_performance": "07_scheme_performance_cleaned.csv",
    "fact_transactions": "08_investor_transactions_cleaned.csv",
    "fact_portfolio": "09_portfolio_holdings_cleaned.csv",
    "fact_benchmark": "10_benchmark_indices_cleaned.csv"
}

print("=" * 60)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 60)

for table, file in files.items():
    path = os.path.join(PROCESSED_DIR, file)

    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✔ {table:25} {len(df):7} rows")

print("\nSQLite Database Created Successfully!")
print(f"Database saved at: {DB_PATH}")