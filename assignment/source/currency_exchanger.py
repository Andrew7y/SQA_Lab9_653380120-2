""" Name : กัมแพงเพชร สิงห์ขรณ์
    ID  : 653380120-2
    sec: 1
"""

import requests
from datetime import datetime

class CurrencyExchanger(Exception):
    def __init__(self, base_currency="THB", target_currency="USD"):
        self.currency_api = "https://coc-kku-bank.com/foreign-exchange"
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.ex_date = datetime.today().date()
        self.api_response = None

    def get_currency_rate(self):
        try:
            # get the exchange rate
            p = {'from': self.base_currency, 'to': self.target_currency}
            response = requests.get(self.currency_api, params=p)
            if response.status_code in (200, 201):
                self.api_response = response.json()
        except requests.exceptions.RequestException:
            self.api_response = None
        # self.api_response = {'base': 'THB', 'result': {'USD': 0.029}}

    def currency_exchange(self, amount):
        self.get_currency_rate()
        # Implement function to calculate the currency from base currency to the target currency
        if self.api_response is not None:
            amount = amount * self.api_response['result'][self.target_currency]

        return amount

# s = CurrencyExchanger(target_currency='USD')
# a = s.currency_exchange(500)
# print(a)
