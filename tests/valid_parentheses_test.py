import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from valid_parentheses import isValid  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(isValid("()"))
        self.assertTrue(isValid("()[]{}"))
        self.assertFalse(isValid("(]"))
