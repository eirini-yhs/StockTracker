
import http.client
import json
import ssl
from typing import Dict, List
import datetime as dt

import requests

HISTORY_ENDPOINT = 'https://sandbox.tradier.com/v1/markets/history'
LOOKUP_ENDPOINT = 'https://sandbox.tradier.com/v1/markets/lookup'

API_KEY = "fJkFBdO5MPpXItQ5VDGDBPq1MqPx"

class StockIngester:

    def get_last_days(self, ticker, start_date, end_date) -> Dict[str, int]:
        response = requests.get(HISTORY_ENDPOINT,
                                params={'symbol': ticker, 'interval': 'daily', 'start': start_date,
                                        'end': end_date},
                                headers={'Authorization': f'Bearer {API_KEY}',
                                         'Accept': 'application/json'})

        stock_dict = response.json()
        days_data_list = stock_dict["history"]["day"]
        result_dict = {item["date"]:item["close"] for item in days_data_list}
        return result_dict

    def find_symbol(self, ticker: str) -> List[str]:
        response = requests.get(LOOKUP_ENDPOINT,
                                params={'q': ticker},
                                headers={'Authorization': f'Bearer {API_KEY}',
                                         'Accept': 'application/json'})
        json_response = response.json()
        print(json_response)
        return []


