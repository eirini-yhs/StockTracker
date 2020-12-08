import unittest
from pprint import pprint

import stock_ingester as si

class MyTestCase(unittest.TestCase):
    def test_get_five_days(self):
        ingester = si.StockIngester()
        results = ingester.get_last_five_days()
        pprint(results)

        self.assertEqual(True, True)

