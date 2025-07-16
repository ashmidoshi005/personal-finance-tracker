from src.database.models import session, Expense
from datetime import datetime
import pandas as pd

class ExpenseManager:
    def add_expense(self, amount, category, date):
        date = datetime.strptime(date, "%Y-%m-%d").date()
        new_expense = Expense(amount=amount, category=category, date=date)
        session.add(new_expense)
        session.commit()

    def view_expenses(self):
        return session.query(Expense).all()

    def edit_expense(self, id, amount, category, date):
        date = datetime.strptime(date, "%Y-%m-%d").date()
        exp = session.query(Expense).get(id)
        if exp:
            exp.amount = amount
            exp.category = category
            exp.date = date
            session.commit()

    def delete_expense(self, id):
        exp = session.query(Expense).get(id)
        if exp:
            session.delete(exp)
            session.commit()

    def export_expense_to_excel(self, filename):
        data = session.query(Expense).all()
        df = pd.DataFrame([(r.id, r.amount, r.category, r.date) for r in data],
                          columns=["ID", "Amount", "Category", "Date"])
        df.to_excel(filename, index=False)