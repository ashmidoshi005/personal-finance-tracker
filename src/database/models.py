from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()
db_path = os.path.abspath("finance.db")
engine = create_engine(f"sqlite:///{db_path}", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    source = Column(String)
    date = Column(Date)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    category = Column(String)
    date = Column(Date)

def init_db():
    Base.metadata.create_all(engine)