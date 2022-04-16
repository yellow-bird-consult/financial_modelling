"""
This file defines the base class for an income.
"""
from financial_modelling.collections.model_map import ModelMap
from financial_modelling.collections.schema import SchemaDescriptor
from financial_modelling.income.enums import IncomeTypes


class Income:
    """
    This class defines the base constructor and what is needed to build an an income class.

    Attributes:
        name (str): the name of the income for description purposes
        amount (int): the number of instances needed for this income
        income_type (IncomeTypes): the type of income the income is
        model_name (str): the name of the model that this income is associated with
        cost (float): the cost of one unit of this income
        year (int): the year this income is taking place
    """
    SCHEMA = SchemaDescriptor()

    def __init__(self, name: str, amount: int,
                 income_type: IncomeTypes, model_name: str, cost: float, year: int) -> None:
        """
        The constructor for the Income class.

        :param name: (str) the name of the income for description purposes
        :param amount: (int) the number of instances needed for this income
        :param income_type: (IncomeTypes) the type of income the income is
        :param model_name: (str) the name of the model that this income is associated with
        :param cost: (float) the cost of one unit of this income
        :param year: (int) the year this income is taking place
        """
        self.name: str = name
        self.amount: int = amount
        self.income_type: IncomeTypes = income_type
        self.model_name: str = model_name
        self.cost: float = cost
        self.year: int = year

    def add_to_model(self) -> None:
        """
        Adds the expense to the model that the expense is associated with.

        :return: None
        """
        model_map = ModelMap()
        model = model_map[self.model_name]
        model.add_income(income=self)
        model_map[self.model_name] = model

    @property
    def calculated_value(self) -> float:
        return self.cost * self.amount
