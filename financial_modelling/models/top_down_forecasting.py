from financial_modelling.collections.model_map import ModelMap


class TopDownForecastingModel:

    def __init__(self, name: str, year: int) -> None:
        self.name: str = name
        self.year: int = year
        self.expense_data = dict()
        self.income_data = dict()
        self._add_to_map()

    def _add_to_map(self) -> None:
        model_map = ModelMap()
        model_map.add_model(model=self)

    def add_expense(self, expense: "Expense") -> None:
        expense_list = self.expense_data.get(expense.expense_type, [])
        expense_list.append(expense)
        self.expense_data[expense.expense_type] = expense_list
