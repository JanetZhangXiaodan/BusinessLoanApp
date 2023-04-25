import unittest
import json
from accounting import app

class TestBalanceSheet(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_generateBalanceSheet(self):
        request_data =  {'businessdetails': {'name': 'D', 'year': '2023-04-10', 'loanAmount': '123'}, 'accountprovider': 'Xerox'}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('/getbalancesheets', data=json.dumps(request_data), headers=headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('profitOrLoss', data)
        self.assertIn('assetsValue', data)
        self.assertIn('yearlyreport', data)
        self.assertEqual(len(data['yearlyreport']), 12)
        for item in data['yearlyreport']:
            self.assertIn('year', item)
            self.assertIn('month', item)
            self.assertIn('profitOrLoss', item)
            self.assertIn('assetsValue', item)

if __name__ == '__main__':
    unittest.main()