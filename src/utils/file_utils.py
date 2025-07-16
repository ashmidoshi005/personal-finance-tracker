import matplotlib.pyplot as plt
import pandas as pd
from src.database.models import session, Income, Expense

def generate_summary_charts():
    income_data = session.query(Income).all()
    expense_data = session.query(Expense).all()

    income_df = pd.DataFrame([(i.amount, i.source) for i in income_data], columns=["Amount", "Source"])
    expense_df = pd.DataFrame([(e.amount, e.category) for e in expense_data], columns=["Amount", "Category"])

    if not income_df.empty:
        income_df.groupby("Source").sum().plot(kind='pie', y='Amount', autopct='%1.1f%%', title='Income Distribution')
        plt.ylabel("")
        plt.savefig("income_chart.png")
        plt.close()

    if not expense_df.empty:
        expense_df.groupby("Category").sum().plot(kind='bar', title='Expense by Category')
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.savefig("expense_chart.png")
        plt.close()
