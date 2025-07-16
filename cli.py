import typer
from src.controllers.income_management import IncomeManager
from src.controllers.expense_management import ExpenseManager
from src.database.models import init_db
from src.utils.file_utils import generate_summary_charts
from tabulate import tabulate

app = typer.Typer()
income_mgr = IncomeManager()
expense_mgr = ExpenseManager()

@app.command()
def add_income(amount: float, source: str, date: str):
    income_mgr.add_income(amount, source, date)
    typer.echo("Income added successfully.")

@app.command()
def view_income():
    records = income_mgr.view_income()
    data = [(r.id, r.amount, r.source, r.date) for r in records]
    typer.echo(tabulate(data, headers=["ID", "Amount", "Source", "Date"], tablefmt="grid"))

@app.command()
def edit_income(id: int, amount: float, source: str, date: str):
    income_mgr.edit_income(id, amount, source, date)
    typer.echo("Income updated successfully.")

@app.command()
def delete_income(id: int):
    income_mgr.delete_income(id)
    typer.echo("Income deleted successfully.")

@app.command()
def add_expense(amount: float, category: str, date: str):
    expense_mgr.add_expense(amount, category, date)
    typer.echo("Expense added successfully.")

@app.command()
def view_expenses():
    records = expense_mgr.view_expenses()
    data = [(r.id, r.amount, r.category, r.date) for r in records]
    typer.echo(tabulate(data, headers=["ID", "Amount", "Category", "Date"], tablefmt="grid"))

@app.command()
def edit_expense(id: int, amount: float, category: str, date: str):
    expense_mgr.edit_expense(id, amount, category, date)
    typer.echo("Expense updated successfully.")

@app.command()
def delete_expense(id: int):
    expense_mgr.delete_expense(id)
    typer.echo("Expense deleted successfully.")

@app.command()
def export_report():
    income_mgr.export_income_to_excel("income_report.xlsx")
    expense_mgr.export_expense_to_excel("expense_report.xlsx")
    typer.echo("Reports exported successfully to Excel.")

@app.command()
def monthly_income_report(month: int, year: int):
    filename = f"monthly_income_{month}_{year}.xlsx"
    income_mgr.generate_monthly_income_report(month, year, filename)
    typer.echo(f"Monthly income report saved to {filename}")

@app.command()
def generate_charts():
    generate_summary_charts()
    typer.echo("Charts saved as income_chart.png and expense_chart.png")

if __name__ == "__main__":
    init_db()
    app()
