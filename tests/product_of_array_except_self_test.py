import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from product_of_array_except_self import productExceptSelf  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
