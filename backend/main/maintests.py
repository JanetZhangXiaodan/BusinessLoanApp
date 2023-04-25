import unittest
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'Message': 'I am fine'})

    def test_get_balancesheet_endpoint(self):
        data = {'key': 'value'}
        response = self.app.post('/balancesheet', json=data)
        self.assertEqual(response.status_code, 200)
        # TODO: add more assertions for the response data
'''
    def test_process_loan_endpoint(self):
        data = {'key': 'value'}
        response = self.app.post('/processloan', json=data)
        self.assertEqual(response.status_code, 200)
        # TODO: add more assertions for the response data
'''
if __name__ == '__main__':
    unittest.main()
