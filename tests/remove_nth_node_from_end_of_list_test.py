import unittest
import sys
import os

sys.path.insert(0, os.getcwd())

from remove_nth_node_from_end_of_list import removeNthFromEnd  # noqa: E402
from reverse_linked_list import ListNode  # noqa: E402


def createListNode(arr: list[int]) -> ListNode | None:
    if len(arr) == 0:
        return None
    return ListNode(arr)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            str(removeNthFromEnd(ListNode([1, 2, 3, 4, 5]), 2)),
            str(ListNode([1, 2, 3, 5])),
        )
        self.assertEqual(
            str(removeNthFromEnd(createListNode([1]), 1)), str(createListNode([]))
        )
        self.assertEqual(
            str(removeNthFromEnd(createListNode([1, 2]), 1)), str(createListNode([1]))
        )
        self.assertEqual(
            str(removeNthFromEnd(createListNode([1, 2]), 2)), str(createListNode([2]))
        )
