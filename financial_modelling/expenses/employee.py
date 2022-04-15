from financial_modelling.expenses.base import Expense
from financial_modelling.expenses.enums import ExpenseType


class Employee(Expense):
    def __init__(self, name: str, amount: int, model_name: str) -> None:
        super().__init__(name=name, amount=amount, expense_type=ExpenseType.PAYROLL, model_name=model_name)

