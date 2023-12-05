import typing as t
from reverse_linked_list import ListNode

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


def mergeTwoLists(
    list1: t.Optional[ListNode], list2: t.Optional[ListNode]
) -> t.Optional[ListNode]:
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    new_head = list1 if list1.val < list2.val else list2
    output_ptr = new_head
    list1_ptr: ListNode | None = list1 if new_head is not list1 else list1.next
    list2_ptr: ListNode | None = list2 if new_head is not list2 else list2.next
    while list1_ptr is not None or list2_ptr is not None:
        # base cases for if we finish one or the other
        if list1_ptr is None:
            output_ptr.next = t.cast(ListNode, list2_ptr)
            list2_ptr = t.cast(ListNode, list2_ptr).next
        elif list2_ptr is None:
            output_ptr.next = list1_ptr
            list1_ptr = list1_ptr.next
        else:
            # Add the smaller value next pointer, than increment the corresponding pointer
            if list1_ptr.val < list2_ptr.val:
                output_ptr.next = list1_ptr
                list1_ptr = list1_ptr.next
            else:
                output_ptr.next = list2_ptr
                list2_ptr = list2_ptr.next
        output_ptr = output_ptr.next
    return new_head
