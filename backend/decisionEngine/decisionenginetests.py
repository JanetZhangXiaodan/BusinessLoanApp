import unittest
import json
from decisionengine import app

class TestDecideLoanEndpoint(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_post_with_valid_request_body(self):
        request_body = {'loanAmount': 100000, 'preassessment': 100}
        response = self.app.post('/decideloanamount',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(request_body))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'outcome': True, 'loanamount': 20000})

    def test_post_with_invalid_content_type(self):
        response = self.app.post('/decideloanamount',
                                 headers={'Content-Type': 'text/plain'},
                                 data='loanAmount=100000&preassessment=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'error': 'Content-Type not supported!'})

    def test_post_with_missing_loan_amount(self):
        request_body = {'preassessment': 100}
        response = self.app.post('/decideloanamount',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(request_body))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'outcome': True, 'loanamount': 0})

    def test_post_with_missing_preassessment(self):
        request_body = {'loanAmount': 100000}
        response = self.app.post('/decideloanamount',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(request_body))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'outcome': True, 'loanamount': 0})

    def test_post_with_negative_loan_amount(self):
        request_body = {'loanAmount': -100000, 'preassessment': 100}
        response = self.app.post('/decideloanamount',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(request_body))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'outcome': True, 'loanamount': 0})

if __name__ == '__main__':
    unittest.main()