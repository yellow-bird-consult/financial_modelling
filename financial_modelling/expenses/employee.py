from financial_modelling.expenses.base import Expense
from financial_modelling.expenses.enums import ExpenseType
from financial_modelling.expenses.pension import Pension
from financial_modelling.expenses.tax import Tax


class Employee(Expense):

    def __init__(self, name: str, amount: int, model_name: str, year: int, salary: float) -> None:
        super().__init__(name=name, amount=amount, expense_type=ExpenseType.PAYROLL,
                         model_name=model_name, year=year, cost=salary)
        self.salary: float = salary
        self._add_pension()
        self._add_national_insurance_tax()

    def _add_national_insurance_tax(self) -> None:
        total_to_be_taxed = 0.0
        first_taxable = self.weekly_earnings - 190

        if first_taxable > 777:
            second_taxable = first_taxable - 777
            total_to_be_taxed += 777 * 0.1325
            total_to_be_taxed += second_taxable * 0.0325
        else:
            total_to_be_taxed += first_taxable * 0.1325

        national_insurance_tax = Tax(name=f"national insurance tax for {self.name}",
                                     amount=self.amount, model_name=self.model_name,
                                     year=self.year, cost=total_to_be_taxed)
        national_insurance_tax.add_to_model()

    def _add_pension(self) -> None:
        pension = Pension(name=f"pension for {self.name}", amount=self.amount,
                          model_name=self.model_name, year=self.year, employer_contribution=self.salary * 0.04)
        pension.add_to_model()

    @property
    def calculated_value(self) -> float:
        return self.cost * self.amount

    @property
    def weekly_earnings(self) -> float:
        return (self.cost / 12) / 4
