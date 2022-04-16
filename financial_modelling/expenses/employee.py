from typing import Optional

from financial_modelling.expenses.base import Expense
from financial_modelling.expenses.enums import ExpenseType
from financial_modelling.expenses.pension import Pension
from financial_modelling.expenses.tax import Tax


class Employee(Expense):
    """
    This class is responsible for calculating the expenses needed for hiring an employee and adding it to a model.

    Attributes:
        salary (float): the yearly pay of an employee with this job
        pension_contribution (float): the percentage of pension contribution (legal minimum is 3%)
        national_insurance_tax (Optional[Tax]): the national insurance needed to pay to employ the employee
        pension (Optional[Pension]): the amount the employer needs to contribute to the employee's pension
    """
    def __init__(self, name: str, amount: int, model_name: str, year: int,
                 salary: float, pension_contribution: float = 0.03) -> None:
        """
        The constructor for the Employee class.

        :param name: (str) the type of job that the employee has
        :param amount: (int) the number of employees with this profile
        :param model_name: (str) the model name that this employee is associated with
        :param year: (int) the year that this employee is going to be involved in
        :param salary: (float) the yearly pay of an employee with this job
        :param pension_contribution: (float) the percentage of pension contribution (legal minimum is 3%)
        """
        super().__init__(name=name, amount=amount, expense_type=ExpenseType.PAYROLL,
                         model_name=model_name, year=year, cost=salary)
        self.salary: float = salary
        self.pension_contribution: float = pension_contribution
        self.national_insurance_tax: Optional[Tax] = None
        self.pension: Optional[Pension] = None
        self._add_pension()
        self._add_national_insurance_tax()

    def _add_national_insurance_tax(self) -> None:
        """
        Calculates the national insurance tax that the employer has to pay.

        :return: None
        """
        total_to_be_taxed = 0.0
        first_taxable = self.weekly_earnings - 190

        if first_taxable > 777:
            second_taxable = first_taxable - 777
            total_to_be_taxed += 777 * 0.1325
            total_to_be_taxed += second_taxable * 0.0325
        else:
            total_to_be_taxed += first_taxable * 0.1325

        self.national_insurance_tax = Tax(name=f"national insurance tax for {self.name}",
                                          amount=self.amount, model_name=self.model_name,
                                          year=self.year, cost=total_to_be_taxed * 4 * 12)

    def _add_pension(self) -> None:
        """
        Calculate the pension contribution that the employer has to commit to.

        :return:
        """
        self.pension = Pension(name=f"pension for {self.name}", amount=self.amount,
                               model_name=self.model_name, year=self.year,
                               employer_contribution=self.salary * self.pension_contribution)

    def add_to_model(self) -> None:
        """
        Adds the employee, pension, and national insurance to the model.

        :return: None
        """
        super().add_to_model()
        self.pension.add_to_model()
        self.national_insurance_tax.add_to_model()

    @property
    def weekly_earnings(self) -> float:
        return (self.cost / 12) / 4
