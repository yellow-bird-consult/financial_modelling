from unittest import main, TestCase

from financial_modelling.collections.model_map import ModelMap, Singleton
from financial_modelling.expenses.base import Expense, ExpenseType
from financial_modelling.models.top_down_forecasting import TopDownForecastingModel


class Test(TestCase):

    def setUp(self) -> None:
        self.name = "test_name"
        self.amount = 2
        self.expense_type = ExpenseType.PAYROLL
        self.model_name = "test_model"
        self.cost = 2.5
        self.year = 1
        self.test = Expense(name=self.name, amount=self.amount, expense_type=self.expense_type,
                            model_name=self.model_name, cost=self.cost, year=self.year)

    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        self.assertEqual(self.name, self.test.name)
        self.assertEqual(self.amount, self.test.amount)
        self.assertEqual(self.expense_type, self.test.expense_type)
        self.assertEqual(self.model_name, self.test.model_name)
        self.assertEqual(self.cost, self.test.cost)
        self.assertEqual(self.year, self.test.year)

    def test_add_to_model(self):
        mock_model = TopDownForecastingModel(name=self.model_name, year=self.year)
        model_map = ModelMap()
        model_map.add_model(model=mock_model)

        self.test.add_to_model()

        expected_data = {
            ExpenseType.PAYROLL: [self.test]
        }
        self.assertEqual(expected_data, mock_model.expense_data)

    def test_calculated_value(self):
        self.assertEqual(5.0, self.test.calculated_value)


if __name__ == "__main__":
    main()
