from src.database.models import session, Income
from datetime import datetime
import pandas as pd

class IncomeManager:
    def add_income(self, amount, source, date):
        date = datetime.strptime(date, "%Y-%m-%d").date()
        new_income = Income(amount=amount, source=source, date=date)
        session.add(new_income)
        session.commit()

    def view_income(self):
        return session.query(Income).all()

    def edit_income(self, id, amount, source, date):
        date = datetime.strptime(date, "%Y-%m-%d").date()
        income = session.query(Income).get(id)
        if income:
            income.amount = amount
            income.source = source
            income.date = date
            session.commit()

    def delete_income(self, id):
        income = session.query(Income).get(id)
        if income:
            session.delete(income)
            session.commit()

    def export_income_to_excel(self, filename):
        data = session.query(Income).all()
        df = pd.DataFrame([(r.id, r.amount, r.source, r.date) for r in data],
                          columns=["ID", "Amount", "Source", "Date"])
        df.to_excel(filename, index=False)

    def generate_monthly_income_report(self, month: int, year: int, filename: str):
        data = session.query(Income).filter(
            Income.date >= datetime(year, month, 1),
            Income.date < datetime(year + (month // 12), ((month % 12) + 1), 1)
        ).all()
        df = pd.DataFrame([(r.id, r.amount, r.source, r.date) for r in data],
                          columns=["ID", "Amount", "Source", "Date"])
        df.to_excel(filename, index=False)