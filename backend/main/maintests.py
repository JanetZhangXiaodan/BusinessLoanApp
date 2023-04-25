import unittest
import json
from unittest.mock import patch, MagicMock

from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_Home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {"Message": "I am fine"})

    @patch('requests.post')
    def test_GetBalanceSheet(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"balance_sheet": "test_data"})
        headers = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 
                   'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Access-Control-Allow-Methods'}
        response = self.app.post('/balancesheet', json={"test_key": "test_value"}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {"balance_sheet": "test_data"})

    @patch('requests.post')
    def test_FinalOutcome(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"result": "approved"})
        headers = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 
                   'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Access-Control-Allow-Methods'}
        response = self.app.post('/finaloutcome', json={"businessdetails": "test_data", "profitOrLoss": 100, 
                                                        "assetsValue": 200, "loanAmount": 500}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {"result": "approved"})

if __name__ == '__main__':
    unittest.main()