import random
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, allow_headers=['Content-Type', 'Content-Length', 'Access-Control-Allow-Origin',
                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])

class BalanceSheet:
    def __init__(self, year):
        self.year = year
        self.months = range(1, 13)
        self.profit_or_loss = [random.randrange(-496446, 984864) for _ in self.months]
        self.assets_value = [random.randrange(-1, 984864) for _ in self.months]

    def net_profit(self):
        return sum(self.profit_or_loss)

    def net_average_assets(self):
        return sum(self.assets_value) / len(self.assets_value)

    def to_dict(self):
        return {
            'profitOrLoss': self.net_profit(),
            'assetsValue': self.net_average_assets(),
            'yearlyreport': [{'year': self.year, 'month': m, 'profitOrLoss': p, 'assetsValue': a} for m, p, a in zip(self.months, self.profit_or_loss, self.assets_value)]
        }

@app.route('/getbalancesheets', methods=['GET', 'POST'])
def generateBalanceSheet():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        if request.method == 'GET':
            return jsonify({'BalanceSheet': 'Balance Sheet present'})
        elif request.method == 'POST':
            json_data = request.get_json()
            print('>>>>>>>>>> json_data', json_data)
            year = json_data.get('businessdetails').get('year')[0:4]
            balance_sheet = BalanceSheet(year)
            print('>>>>>>>>>> balance_sheet', balance_sheet.to_dict())
            return jsonify(balance_sheet.to_dict())
    else:
        return jsonify({'error': 'Content-Type not supported!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
