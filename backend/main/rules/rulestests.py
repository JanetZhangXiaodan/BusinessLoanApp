import unittest
from unittest.mock import MagicMock
from rules import ifBothConditionsMet, RuleEngine

def test_ifBothConditionsMet(self):
    self.assertEqual(ifBothConditionsMet([100, 60]), 100)
    self.assertEqual(ifBothConditionsMet([60]), 60)
    with self.assertRaises(TypeError):
        ifBothConditionsMet(60)
    with self.assertRaises(ValueError):
        ifBothConditionsMet([])

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.balance_sheet_info = MagicMock()
        self.rule_engine = RuleEngine()

    def test_RuleEngine(self):
        self.balance_sheet_info.profit_or_loss = 5000
        self.balance_sheet_info.average_value = 120000
        self.balance_sheet_info.loan_amount = "100000"
        self.assertEqual(self.rule_engine.finalisePreAssessment(self.balance_sheet_info), 100)
        self.balance_sheet_info.average_value = 12
        self.assertEqual(self.rule_engine.finalisePreAssessment(self.balance_sheet_info), 60)
        self.balance_sheet_info.profit_or_loss = 0
        self.balance_sheet_info.average_value = 120000
        self.assertEqual(self.rule_engine.finalisePreAssessment(self.balance_sheet_info), 100)
        self.balance_sheet_info.profit_or_loss = 0
        self.balance_sheet_info.average_value = 12
        self.assertEqual(self.rule_engine.finalisePreAssessment(self.balance_sheet_info), 20)
       
if __name__ == '__main__':
    unittest.main()