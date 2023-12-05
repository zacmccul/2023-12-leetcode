import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from valid_anagram import isAnagram  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(isAnagram("anagram", "nagaram"))
        self.assertFalse(isAnagram("rat", "car"))
