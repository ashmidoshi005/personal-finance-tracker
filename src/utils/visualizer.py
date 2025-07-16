import matplotlib.pyplot as plt
import os
import pandas as pd


def plot_expenses_by_category(expense_df, month, year):
    category_totals = expense_df.groupby("category")["amount"].sum()
    if category_totals.empty:
        print("No data to plot.")
        return

    # Pie chart
    plt.figure(figsize=(6, 6))
    category_totals.plot.pie(autopct='%1.1f%%')
    plt.title(f"Expenses by Category - {month}/{year}")
    plt.ylabel('')
    os.makedirs("reports/graphs", exist_ok=True)
    plt.savefig(f"reports/graphs/pie_{month}_{year}.png")
    plt.close()

    # Bar chart
    plt.figure(figsize=(8, 5))
    category_totals.plot(kind='bar', color='teal')
    plt.title(f"Expenses by Category - {month}/{year}")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig(f"reports/graphs/bar_{month}_{year}.png")
    plt.close()

def plot_income_vs_expense(income_df, expense_df):
    income_df['month'] = income_df['date'].dt.to_period('M')
    expense_df['month'] = expense_df['date'].dt.to_period('M')

    income_by_month = income_df.groupby('month')['amount'].sum()
    expense_by_month = expense_df.groupby('month')['amount'].sum()

    all_months = pd.Series(sorted(set(income_by_month.index) | set(expense_by_month.index)))
    income = income_by_month.reindex(all_months, fill_value=0)
    expense = expense_by_month.reindex(all_months, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income.index.astype(str), income, label="Income", marker='o')
    plt.plot(expense.index.astype(str), expense, label="Expense", marker='o')
    plt.title("Monthly Income vs Expense")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.legend()
    plt.grid(True)
    os.makedirs("reports/graphs", exist_ok=True)
    plt.savefig("reports/graphs/income_vs_expense_line.png")
    plt.close()

def plot_monthly_savings(income_df, expense_df):
    income_df['month'] = income_df['date'].dt.to_period('M')
    expense_df['month'] = expense_df['date'].dt.to_period('M')

    income_by_month = income_df.groupby('month')['amount'].sum()
    expense_by_month = expense_df.groupby('month')['amount'].sum()

    savings_by_month = income_by_month - expense_by_month
    savings_by_month = savings_by_month.fillna(0)

    plt.figure(figsize=(10, 5))
    savings_by_month.plot(kind='bar', color='green')
    plt.title("Monthly Net Savings")
    plt.xlabel("Month")
    plt.ylabel("Savings")
    plt.tight_layout()
    os.makedirs("reports/graphs", exist_ok=True)
    plt.savefig("reports/graphs/monthly_savings_bar.png")
    plt.close()

def plot_expense_trends(expense_df):
    expense_df['month'] = expense_df['date'].dt.to_period('M')
    pivot_df = expense_df.pivot_table(values='amount', index='month', columns='category', aggfunc='sum').fillna(0)

    plt.figure(figsize=(10, 6))
    for category in pivot_df.columns:
        plt.plot(pivot_df.index.astype(str), pivot_df[category], label=category, marker='o')

    plt.title("Expenses Over Time by Category")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.legend()
    plt.tight_layout()
    os.makedirs("reports/graphs", exist_ok=True)
    plt.savefig("reports/graphs/expense_trends_by_category.png")
    plt.close()