import json
from abc import ABC, abstractmethod
from decimal import Decimal


class PreAssessmentRule(ABC):
    @abstractmethod
    def should_process(self, balance_sheet_info):
        pass

    @abstractmethod
    def calculate_pre_assessment(self):
        pass

class AverageAssessmentRule(PreAssessmentRule):
    def should_process(self, balance_sheet_info):
        print("Inside AverageAssessmentRule")
        print(balance_sheet_info.profit_last_year)
        return balance_sheet_info.profit_last_year > Decimal(0)

    def calculate_pre_assessment(self):
        return Decimal(60)

class HighAssessmentRule(PreAssessmentRule):
    def should_process(self, balance_sheet_info):
        return balance_sheet_info.average_asset > balance_sheet_info.loan_amount

    def calculate_pre_assessment(self):
        return Decimal(100)

class RuleEngine:
    def __init__(self):
        self.rules_collection = [AverageAssessmentRule(), HighAssessmentRule()]

    def calculate_pre_assessment(self, balance_sheet_info):
        for rule in self.rules_collection:
            if rule.should_process(balance_sheet_info):
                print(f"inside rule-engine for rule {rule}")
                return rule.calculate_pre_assessment()