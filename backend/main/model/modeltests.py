import unittest
from decimal import Decimal
from model import BalanceSheetSummary

class TestBalanceSheetSummary(unittest.TestCase):
    def test_BalanceSheetSummary(self):
        profit_or_loss = 50000.0
        average_value = 100000.0
        loan_amount = 75000.0
        bss = BalanceSheetSummary(profit_or_loss, average_value, loan_amount)
        self.assertEqual(bss.profit_or_loss, profit_or_loss)
        self.assertEqual(bss.average_value, average_value)
        self.assertEqual(bss.loan_amount, loan_amount)

if __name__ == "__main__":
    unittest.main()