def ifBothConditionsMet(input):
    if not isinstance(input, (list)):
        raise TypeError("Input must be a list")
    if len(input) == 0:
        raise ValueError("Input list cannot be empty")
    return max(input)

class IfBisMadeAProfit():
    def process(self, balance_sheet_info):
        print("Checking if business made a profit..")
        return balance_sheet_info.profit_or_loss > 0

    def calculatePreAssessment(self):
        return 60

class IfBisAssetMoreThanLoan():
    def process(self, balance_sheet_info):
        print("Checking if business average asset value across 12 months is greater than the loan amount..")
        return balance_sheet_info.average_value > float(balance_sheet_info.loan_amount)

    def calculatePreAssessment(self):
        return 100
    
class RuleEngine:
    def finalisePreAssessment(self, balance_sheet_info):
        pre_assessment_value=[]
        for rule in [IfBisMadeAProfit(), IfBisAssetMoreThanLoan()]:
            if rule.process(balance_sheet_info):
                pre_assessment_value.append(rule.calculatePreAssessment())
            else:
                pre_assessment_value.append(20)
        return ifBothConditionsMet(pre_assessment_value)