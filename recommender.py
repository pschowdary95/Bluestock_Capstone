import pandas as pd

sharpe = pd.read_csv("reports/sharpe_ratio.csv")
fund = pd.read_csv("data/processed/01_fund_master_cleaned.csv")

recommend_df = sharpe.merge(
    fund[["amfi_code", "scheme_name", "risk_category"]],
    on="amfi_code"
)

def recommend_funds(risk):

    result = (
        recommend_df[
            recommend_df["risk_category"] == risk
        ]
        .sort_values("Sharpe_Ratio", ascending=False)
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "risk_category",
            "Sharpe_Ratio"
        ]
    ]

print("\nTop 3 Low Risk Funds")
print(recommend_funds("Low"))

print("\nTop 3 Moderate Risk Funds")
print(recommend_funds("Moderate"))

print("\nTop 3 High Risk Funds")
print(recommend_funds("High"))