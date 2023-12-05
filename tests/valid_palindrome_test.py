import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from valid_palindrome import isPalindrome  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(isPalindrome("race a car"))
        self.assertTrue(isPalindrome(" "))
        self.assertFalse(isPalindrome("0P"))
        self.assertTrue(isPalindrome("a."))
