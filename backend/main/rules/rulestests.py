import unittest
from decimal import Decimal
from unittest.mock import Mock, patch

from rules import PreAssessmentRule, AverageAssessmentRule, HighAssessmentRule, RuleEngine

class TestPreAssessmentRule(unittest.TestCase):
    def test_pre_assessment_rule(self):
        pre_assessment_rule = PreAssessmentRule()
        with self.assertRaises(TypeError):
            pre_assessment_rule.shouldprocess()
        with self.assertRaises(TypeError):
            pre_assessment_rule.calculatepreAssessment()

class TestAverageAssessmentRule(unittest.TestCase):
    def test_average_assessment_rule(self):
        balancesheet_info = Mock()
        balancesheet_info.profit_last_year = Decimal(10000.0)
        average_assessment_rule = AverageAssessmentRule()
        should_process = average_assessment_rule.shouldprocess(balancesheet_info)
        self.assertTrue(should_process)
        pre_assessment = average_assessment_rule.calculatepreAssessment()
        self.assertEqual(pre_assessment, Decimal(60.0))

class TestHighAssessmentRule(unittest.TestCase):
    def test_high_assessment_rule(self):
        balancesheet_info = Mock()
        balancesheet_info.average_asset = Decimal(50000.0)
        balancesheet_info.loan_amount = Decimal(30000.0)
        high_assessment_rule = HighAssessmentRule()
        should_process = high_assessment_rule.shouldprocess(balancesheet_info)
        self.assertTrue(should_process)
        pre_assessment = high_assessment_rule.calculatepreAssessment()
        self.assertEqual(pre_assessment, Decimal(100.0))

class TestRuleEngine(unittest.TestCase):
    def test_rule_engine(self):
        rule_engine = RuleEngine()
        balancesheet_info = Mock()
        with patch.object(AverageAssessmentRule, "shouldprocess", return_value=True) as mock_should_process:
            with patch.object(AverageAssessmentRule, "calculatepreAssessment", return_value=Decimal(60.0)) as mock_pre_assessment:
                pre_assessment = rule_engine.calculatePreAssesment(balancesheet_info)
                mock_should_process.assert_called_once_with(AverageAssessmentRule()),
