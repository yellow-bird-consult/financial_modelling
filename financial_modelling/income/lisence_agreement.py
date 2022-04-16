from typing import Optional

from financial_modelling.expenses.tax import Tax
from financial_modelling.income.base import Income
from financial_modelling.income.enums import IncomeTypes


class LisenceAgreement(Income):

    def __init__(self, name: str, amount: int, model_name: str, cost: float, year: int) -> None:
        super().__init__(name=name, amount=amount, model_name=model_name, cost=cost,
                         year=year, income_type=IncomeTypes.LICENCE_AGREEMENT)
        self.vat: Optional[Tax] = None

    def _define_vat(self) -> None:
        self.vat = Tax(name=f"VAT tax for {self.name}", amount=self.amount,
                       model_name=self.model_name, year=self.year, cost=0.25* self.cost)

    def add_to_model(self) -> None:
        super().add_to_model()
        self.vat.add_to_model()
