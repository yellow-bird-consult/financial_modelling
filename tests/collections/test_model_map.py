from unittest import main, TestCase
from unittest.mock import MagicMock

from financial_modelling.collections.model_map import ModelMap, Singleton


class Test(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        one = ModelMap()
        two = ModelMap()

        self.assertEqual({}, one)
        self.assertEqual({}, two)
        self.assertEqual(id(one), id(two))

    def test_model(self):
        one = ModelMap()
        mock_model = MagicMock()
        mock_model.name = "test_name"

        one.add_model(model=mock_model)

        expected_data = {
            "test_name": mock_model
        }
        self.assertEqual(expected_data, one)


if __name__ == "__main__":
    main()
