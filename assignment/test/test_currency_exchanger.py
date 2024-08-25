""" Name : กัมแพงเพชร สิงห์ขรณ์
    ID  : 653380120-2
    sec: 1
"""

import unittest
from unittest.mock import patch

from assignment.source.currency_exchanger import CurrencyExchanger
from assignment.test.responAPI_mock import get_mock_currency_api_response

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.currency_exchanger = CurrencyExchanger(target_currency="KRW")
        self.mock_api_response = get_mock_currency_api_response()

    def tearDown(self):
        self.currency_exchanger = None
        self.mock_api_response = None

    @patch("assignment.source.currency_exchanger.requests")
    def test_get_currency_rate(self, mock_request):
        mock_request.get.return_value = self.mock_api_response
        self.currency_exchanger.get_currency_rate()
        mock_request.get.assert_called_once()
        mock_request.get.assert_called_with('https://coc-kku-bank.com/foreign-exchange',
                                            params={'from': 'THB', 'to': 'KRW'})

        self.assertIsNotNone(self.currency_exchanger.api_response)
        self.assertEqual(self.currency_exchanger.api_response, self.mock_api_response.json())

    @patch("assignment.source.currency_exchanger.requests")
    def test_currency_exchange(self, mock_request):
        mock_request.get.return_value = self.mock_api_response
        result = self.currency_exchanger.currency_exchange(500)
        mock_request.get.assert_called_once()
        mock_request.get.assert_called_with('https://coc-kku-bank.com/foreign-exchange',
                                            params={'from': 'THB', 'to': 'KRW'})
        expected = 500 * 38.69
        self.assertEqual(result, expected)
        self.assertEqual(38.69, self.mock_api_response.json()["result"]["KRW"])