import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

# from A import A  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        """Time consuming to build own tests so... just won't. It's mostly just building some LinkedList code to make
        creating cycles easy, but out of scope.
        """
        pass
