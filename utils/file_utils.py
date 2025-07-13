import os
import pandas as pd

def export_to_csv(income_df, expense_df):
    os.makedirs("data", exist_ok=True)
    income_df.to_csv("data/income_export.csv", index=False)
    expense_df.to_csv("data/expense_export.csv", index=False)

def export_to_excel(income_df, expense_df, month, year):
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/{month}_{year}_report.xlsx"
    with pd.ExcelWriter(filename) as writer:
        income_df.to_excel(writer, sheet_name="Income", index=False)
        expense_df.to_excel(writer, sheet_name="Expenses", index=False)

def export_summary_text(summary, month, year):
    os.makedirs("reports", exist_ok=True)
    with open("reports/summary.txt", "w") as f:
        f.write(f"Summary for {month}/{year}\n")
        for key, value in summary.items():
            if isinstance(value, dict):
                f.write(f"\n{key}:\n")
                for cat, amt in value.items():
                    f.write(f" - {cat}: ₹{amt:.2f}\n")
            else:
                f.write(f"{key}: ₹{value:.2f}\n")