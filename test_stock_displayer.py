from unittest import TestCase
import stock_displayer as sd
import stock_ingester_tradier as si

class TestCovidDisplayer(TestCase):
    def test_display_days(self):
        ingester = si.StockIngester()
        data_dict = ingester.get_last_days("AAPL", "2020-11-01", "2020-11-10")

        displayer = sd.StockDisplayer()
        displayer.display_days("AAPL", data_dict)
        self.assertTrue(True, True)
