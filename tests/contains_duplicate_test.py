import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from contains_duplicate import containsDuplicate  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(containsDuplicate([1, 2, 3, 4]))
        self.assertTrue(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
