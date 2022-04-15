"""
This file defines the base class for an expense
"""
from financial_modelling.expenses.enums import ExpenseType
from financial_modelling.collections.model_map import ModelMap


class Expense:
    """
    This class deinfes the base constructor and what is needed to build an expense class.

    Attributes:
        name (str): the name of the expense for description purposes
        amount (int): the number of instances needed for this expense
        expense_type (ExpenseType): the type of expense the expense is
        model_name (str): the name of the model that this expense is associated with
        cost (float): the cost of one unit of this expense
        year (int): the year this expense is taking place
    """
    def __init__(self, name: str, amount: int, expense_type: ExpenseType, model_name: str, cost: float, year: int) -> None:
        """
        The constructor for the Expense class.

        :param name: (str) the name of the expense for description purposes
        :param amount: (int) the number of instances needed for this expense
        :param expense_type: (ExpenseType) the type of expense the expense is
        :param model_name: (str) the name of the model that this expense is associated with
        :param cost: (float) the cost of one unit of this expense
        :param year: (int) the year this expense is taking place
        """
        self.name: str = name
        self.amount: int = amount
        self.expense_type: ExpenseType = expense_type
        self.model_name: str = model_name
        self.cost: float = cost
        self.year: int = year

    def add_to_model(self) -> None:
        model_map = ModelMap()
        model = model_map[self.model_name]
        model.add_expense(expense=self)
        model_map[self.model_name] = model

    @property
    def schema(self) -> dict:
        # TODO => convert this into a descriptor in the collections
        return {
            "name": self.name,
            "number": self.amount,
            "type": self.expense_type,
            "amount per item": self.cost,
            "year": self.year,
            "total amount": self.calculated_value
        }

    @property
    def calculated_value(self) -> float:
        return self.cost * self.amount
