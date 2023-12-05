import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from reverse_linked_list import reverseList, ListNode  # noqa: E402


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            str(reverseList(ListNode([1, 2, 3, 4, 5]))), str(ListNode([5, 4, 3, 2, 1]))
        )
        self.assertEqual(str(reverseList(ListNode([1, 2]))), str(ListNode([2, 1])))
        self.assertEqual(str(reverseList(ListNode([]))), str(ListNode([])))
