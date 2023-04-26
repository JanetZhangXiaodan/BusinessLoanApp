from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests

from model.model import BalanceSheetSummary
from rules.rules import RuleEngine

app = Flask(__name__)
api = Api(app)
CORS(app, allow_headers=['Content-Type', 'Content-Length', 'Access-Control-Allow-Origin',
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
        try:
            if not request.is_json:
                raise ValueError("Content-Type not supported!")

            data = request.json
            print('>>>>>>>>>> GetBalanceSheet request', data)
            balancesheet = requests.post('http://accounting:8081/getbalancesheets', json=data)
            #CMD: 'http://localhost:8081/getbalancesheets'
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
        try:
            if not request.is_json:
                raise ValueError("Content-Type not supported!")

            data = request.json
            print('>>>>>>>>>> ProcessLoan request', data)
            balancesheet_info = BalanceSheetSummary(
                profit_or_loss=data['profitOrLoss'],
                average_value=data['assetsValue'],
                loan_amount=data['loanAmount'] )
            pre_assessment = self.rule_engine.finalisePreAssessment(balancesheet_info)

            loan_request = {
                "businessDetails": data["businessdetails"],
                "profitOrLoss": balancesheet_info.profit_or_loss,
                "loanAmount": balancesheet_info.loan_amount,
                "preAssessment": pre_assessment
            }
            print('>>>>>>>>>> loan_request', loan_request)

            loan_result = requests.post('http://decisionengine:8082/getfinaloutcome', json=loan_request)
            #CMD: 'http://localhost:8082/getfinaloutcome'
            return loan_result.json()

        except Exception as e:
            return jsonify({"error": str(e)}), 400

api.add_resource(Home, '/')
api.add_resource(GetBalanceSheet, '/balancesheet')
api.add_resource(FinalOutcome, '/finaloutcome')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
