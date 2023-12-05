import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from merge_two_sorted_lists import mergeTwoLists  # noqa: E402
from reverse_linked_list import ListNode  # noqa: E402


def createListNode(arr: list[int]) -> ListNode | None:
    if len(arr) == 0:
        return None
    return ListNode(arr)


class Test(unittest.TestCase):
    def test1(self):
        """Time consuming to build own tests so... just won't. It's mostly just building some LinkedList code to make
        creating cycles easy, but out of scope.
        """
        self.assertEqual(
            str(mergeTwoLists(createListNode([1, 2, 4]), createListNode([1, 3, 4]))),
            str(ListNode([1, 1, 2, 3, 4, 4])),
        )
        self.assertEqual(
            str(mergeTwoLists(createListNode([]), createListNode([]))),
            str(createListNode([])),
        )
        self.assertEqual(
            str(mergeTwoLists(createListNode([]), createListNode([0]))),
            str(createListNode([0])),
        )
