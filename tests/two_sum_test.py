import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from two_sum import twoSum


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(twoSum([3, 3], 6), [0, 1])
