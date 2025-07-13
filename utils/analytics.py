import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///finance.db")

def load_data():
    income_df = pd.read_sql("SELECT * FROM incomes", engine, parse_dates=["date"])
    expense_df = pd.read_sql("SELECT * FROM expenses", engine, parse_dates=["date"])
    return income_df, expense_df

def monthly_summary(month: int, year: int):
    income_df, expense_df = load_data()

    income_month = income_df[(income_df['date'].dt.month == month) & (income_df['date'].dt.year == year)]
    expense_month = expense_df[(expense_df['date'].dt.month == month) & (expense_df['date'].dt.year == year)]

    total_income = income_month['amount'].sum()
    total_expense = expense_month['amount'].sum()
    savings = total_income - total_expense

    summary = {
        "Total Income": total_income,
        "Total Expense": total_expense,
        "Savings": savings,
        "Expense by Category": expense_month.groupby("category")["amount"].sum().to_dict()
    }

    return summary, income_month, expense_month