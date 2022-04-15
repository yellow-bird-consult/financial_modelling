from financial_modelling.expenses.base import Expense
from financial_modelling.expenses.enums import ExpenseType


class Pension(Expense):

    def __init__(self, name: str, amount: int, model_name: str, year: int, employer_contribution: float) -> None:
        super().__init__(name=name, amount=amount, expense_type=ExpenseType.PAYROLL,
                         model_name=model_name, year=year, cost=employer_contribution)


