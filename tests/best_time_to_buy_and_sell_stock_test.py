import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from best_time_to_buy_and_sell_stock import maxProfit  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(maxProfit([4, 1, 2]), 1)
