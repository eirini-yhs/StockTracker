from pprint import pprint
from unittest import TestCase
import stock_ingester_tradier as si

class TestStockIngester(TestCase):
    def test_get_last_days(self):
        ingester = si.StockIngester()
        result = ingester.get_last_days("AAPL", "2020-11-01", "2020-11-10")
        pprint(result)
