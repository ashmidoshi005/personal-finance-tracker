import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict

def generate_expense_pie_chart(db_path="finance.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()

    if data:
        labels, values = zip(*data)
        plt.figure(figsize=(6,6))
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Expenses by Category")
        plt.savefig("reports/graphs/expense_pie_chart.png")
        plt.close()
