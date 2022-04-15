"""
This file defines the enums which define categories for expenses.
"""
from enum import Enum


class ExpenseType(Enum):
    """
    Defines all the categories for expenses.
    """
    PAYROLL = "payroll"
    RENT = "rent"
    UTILITIES = "utilities"
    SOFTWARE_SUBSCRIPTIONS = "software subscriptions"
    MARKETING = "marketing"
    TRAVEL_AND_ENTERTAINMENT = "travel and entertainment"
    SERVERS_AND_MAINTENANCE = "servers and maintenance"
    TAX = "tax"
    BUISNESS_INSURANCE = "business ensurance"
    CONSULTANTS_AND_PROFESSIONAL_INSURANCE = "consultants and professional insurance"
    TRAINING_AND_LEARNING = "training and learning"
    EQUIPMENT_AND_FURNITURE = "equipment and furniture"
    OFFICE_SUPPLIES = "office supplies"
    FUEL_AND_MILEAGE = "fuel and millage"
    EMPLOYEE_PERKS = "employee perks"