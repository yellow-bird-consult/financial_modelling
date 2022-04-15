"""
This file defines the base class for an expense
"""
from financial_modelling.expenses.enums import ExpenseType


class Expense:
    """
    This class deinfes the base constructor and what is needed to build an expense class.

    Attributes:
        name (str): the name of the expense for description purposes
        amount (int): the number of instances needed for this expense
        expense_type (ExpenseType): the type of expense the expense is
        model_name (str): the name of the model that this expense is associated with
    """
    def __init__(self, name: str, amount: int, expense_type: ExpenseType, model_name: str, cost: float) -> None:
        """
        The constructor for the Expense class.

        :param name: (str) the name of the expense for description purposes
        :param amount: (int) the number of instances needed for this expense
        :param expense_type: (ExpenseType) the type of expense the expense is
        :param model_name: (str) the name of the model that this expense is associated with
        :param cost: (float) the name of the model that this expense is associated with
        """
        self.name: str = name
        self.amount: int = amount
        self.expense_type: ExpenseType = expense_type
        self.model_name: str = model_name
        self.cost: float = cost

    @property
    def calculated_value(self) -> float:
        raise NotImplementedError("calculated value needs to be defined")
