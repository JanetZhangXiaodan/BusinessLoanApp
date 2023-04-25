from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests

from model.model import BusinessDetails, BalanceSheetSummary
from rules.rules import RuleEngine

app = Flask(__name__)
api = Api(app)
CORS(app, allow_headers=['Content-Type', 'Access-Control-Allow-Origin',
                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])

parser = reqparse.RequestParser()

class Home(Resource):
    """
    Home resource that returns a simple message.
    """
    def get(self):
        return jsonify({"Message": "I am fine"})


class GetBalanceSheet(Resource):
    """
    Resource to get balance sheet information from accounting service.
    """
    def post(self):
        print('>>>>>>>>>> GetBalanceSheet request',request)
        try:
            if not request.is_json:
                raise ValueError("Content-Type not supported!")

            data = request.json
            print('>>>>>>>>>>', data)
            balancesheet = requests.post('http://localhost:8081/getaccounts', json=data)
            return balancesheet.json()

        except Exception as e:
            return jsonify({"error": str(e)}), 400

class FinalOutcome(Resource):
    """
    Resource to process a loan application.
    """
    def __init__(self):
        self.rule_engine = RuleEngine()

    def post(self):
        print('>>>>>>>>>> ProcessLoan request',request)
        try:
            if not request.is_json:
                raise ValueError("Content-Type not supported!")

            data = request.json
            print('>>>>>>>>>>', data)

            business_details = BusinessDetails(**data['businessdetails'])
            balancesheet_info = BalanceSheetSummary(
                business_details=business_details,
                profit_last_year=data['profitOrLoss'],
                average_assets=data['assetsValue'],
                loan_amount=data['loanAmount'],
            )

            pre_assessment = self.rule_engine.calculate_pre_assessment(balancesheet_info)

            loan_request = {
                "businessdetails": balancesheet_info.business_details.dict(),
                "loanAmount": balancesheet_info.loan_amount,
                "pre_assessment": pre_assessment
            }

            loan_result = requests.post('http://localhost:8082/decideloanamount', json=loan_request)
            return loan_result.json()

        except Exception as e:
            return jsonify({"error": str(e)}), 400

api.add_resource(Home, '/')
api.add_resource(GetBalanceSheet, '/balancesheet')
api.add_resource(FinalOutcome, '/processloan')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
