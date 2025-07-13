import typer
from datetime import datetime
from database.models import Income, Expense, session, init_db
from utils.analytics import monthly_summary
from utils.file_utils import export_to_excel
from utils.visualizer import (plot_expenses_by_category, plot_income_vs_expense, plot_monthly_savings, plot_expense_trends)



app = typer.Typer()

@app.command()
def add_income(
    amount: float = typer.Option(...),
    source: str = typer.Option(...),
    date: str = typer.Option(...)
):
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    income = Income(amount=amount, source=source, date=date_obj)
    session.add(income)
    session.commit()
    typer.echo(f"Income added: ₹{amount} from {source} on {date}")

@app.command()
def add_expense(
    amount: float = typer.Option(...),
    category: str = typer.Option(...),
    date: str = typer.Option(...)
):
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    expense = Expense(amount=amount, category=category, date=date_obj)
    session.add(expense)
    session.commit()
    typer.echo(f"Expense recorded: ₹{amount} for {category} on {date}")


@app.command()
def plot_graphs(month: int = typer.Option(...), year: int = typer.Option(...)):
    summary, income_df, expense_df = monthly_summary(month, year)
    plot_expenses_by_category(expense_df, month, year)
    plot_income_vs_expense(income_df, expense_df)
    plot_monthly_savings(income_df, expense_df)
    plot_expense_trends(expense_df)
    typer.echo("📊 Charts saved in /reports/graphs/")

@app.command()
def export_report(month: int = typer.Option(...), year: int = typer.Option(...)):
    summary, income_df, expense_df = monthly_summary(month, year)

    # Export to Excel
    export_to_excel(income_df, expense_df, month, year)

    typer.echo("✅ Excel report generated successfully!")
    
@app.command()
def test_db():
    try:
        session.execute('SELECT 1')
        typer.echo("✅ Database connection is working!")
    except Exception as e:
        typer.echo(f"❌ Database error: {e}")

if __name__ == "__main__":
    app()