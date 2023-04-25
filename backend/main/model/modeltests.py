import unittest
from datetime import datetime
from decimal import Decimal
from model import BusinessDetails, LoanRequestInfo, BalanceSheetSummary


class TestBusinessDetails(unittest.TestCase):
    def test_business_details_creation(self):
        name = "ABC Company"
        year_established = datetime.now()
        summary_profit_loss = {"employees": 10, "revenue": Decimal("50000")}
        bd = BusinessDetails(name, year_established, summary_profit_loss)
        self.assertEqual(bd.name, name)
        self.assertEqual(bd.year_established, year_established)
        self.assertEqual(bd.summary_profit_loss, summary_profit_loss)


class TestLoanRequestInfo(unittest.TestCase):
    def test_loan_request_info_creation(self):
        bd = BusinessDetails("ABC Company", datetime.now(), {"employees": 10, "revenue": Decimal("50000")})
        preassessment = Decimal("150000")
        lri = LoanRequestInfo(bd, preassessment)
        self.assertEqual(lri.business_details, bd)
        self.assertEqual(lri.pre_assessment, preassessment)


class TestBalanceSheetSummary(unittest.TestCase):
    def test_balance_sheet_summary_creation(self):
        bd = BusinessDetails("ABC Company", datetime.now(), {"employees": 10, "revenue": Decimal("50000")})
        profit_last_year = Decimal("50000")
        avg_asset = Decimal("100000")
        loan_amount = Decimal("75000")
        bss = BalanceSheetSummary(bd, profit_last_year, avg_asset, loan_amount)
        self.assertEqual(bss.business_details, bd)
        self.assertEqual(bss.profit_last_year, profit_last_year)
        self.assertEqual(bss.average_asset, avg_asset)
        self.assertEqual(bss.loan_amount, loan_amount)


if __name__ == "__main__":
    unittest.main()
