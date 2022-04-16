"""
This file defines the descriptor for managing a schema for the conversion to a pandas dataframe.
"""
from typing import Optional


class SchemaDescriptor:
    """
    This class is a descriptor for managing the schema serialization for converting an expense or income to a dict
    to aid the creation of a pandas dataframe.
    """
    def __get__(self, obj, class_type) -> dict:
        """
        When the schema is called to get data of the object as a dict.

        :param obj: (Any) the object calling the descriptor
        :param class_type: (class_type) the class owning the object
        :return: (dict) the data of the object calling the descriptor
        """
        from financial_modelling.expenses.base import Expense
        from financial_modelling.income.base import Income

        cash_flow: Optional[str] = None
        transaction_type: Optional[str] = None

        if isinstance(obj, Expense):
            cash_flow = "expense"
            transaction_type = obj.expense_type.value
        elif isinstance(obj, Income):
            cash_flow = "income"
            transaction_type = obj.income_type.value

        return {
            "name": obj.name,
            "number": obj.amount,
            "type": transaction_type,
            "amount per item": obj.cost,
            "year": obj.year,
            "total amount": obj.calculated_value,
            "cash flow": cash_flow
        }

    def __set__(self, obj, value) -> None:
        raise AttributeError("Cannot change the value")
