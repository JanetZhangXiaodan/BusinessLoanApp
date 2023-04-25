from typing import Dict
from datetime import datetime
from decimal import Decimal

class BusinessDetails:
    def __init__(self, name: str, year_established: datetime, summary_profit_loss: Dict):
        self.name = name
        self.year_established = year_established
        self.summary_profit_loss = summary_profit_loss

class LoanRequestInfo:
    def __init__(self, business_details: BusinessDetails, pre_assessment: Decimal):
        self.business_details = business_details
        self.pre_assessment = pre_assessment

class BalanceSheetSummary:
    def __init__(self, business_details: BusinessDetails, profit_last_year: Decimal, 
                 average_asset: Decimal, loan_amount: Decimal):
        self.business_details = business_details
        self.profit_last_year = profit_last_year
        self.average_asset = average_asset
        self.loan_amount = loan_amount
