import unittest
from Client_server.client import client_message, login
from Client_server.server import authenticate, open_auth
import json




class TestSalary(unittest.TestCase):
    def setUp(self):
        with open(r'E:\Desktop\Geekbrains\Клиент серверное пиложение\ДЗ\Lesson3_Kuzmin\Client_server\auth.json') as f:
            self.auth = json.load(f)


    def test_auth(self):

        self.assertEqual(authenticate({'ewe':'adsd'}, self.auth), '403')

        data = {
                        "action": "authenticate",
                        "time": ' ',
                        "user": {
                            "account_name": 'igor',
                            "password": '123'
                            }
                        }
        self.assertEqual(authenticate(data, self.auth), '200')

        data = {
                        "action": "authenticate",
                        "time": ' ',
                        "user": {
                            "account_name": '444',
                            "password": '123'
                            }
                        }

        self.assertEqual(authenticate(data, self.auth), '402')

