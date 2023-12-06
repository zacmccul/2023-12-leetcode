import typing as t
from reverse_linked_list import ListNode

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


def removeNthFromEnd(head: t.Optional[ListNode], n: int) -> t.Optional[ListNode]:
    """Removes the len(head) - n - 1th node from linkedList. Two pass approach.
    Algorithm:
    1. Loop through to get # of elements O(n)/O(1)
    2. Iterate # elements - n - 1 with two pointers, and assign previous.next to cur.next, O(n-m-1)/O(1)
    There is a slow/fast pointer style that has fast pointer sprinting out n steps ahead first that is better than
        this approach.
    Args:
        head (t.Optional[ListNode]): Head of input linked list
        n (int): How many index positions backwards from end to cut.

    Returns:
        t.Optional[ListNode]: The shortened by one linkedlist.
    """
    if head is None:
        return None
    num_elements = 0
    ptr = head
    while ptr is not None:
        num_elements += 1
        ptr = ptr.next

    if num_elements == 1:
        return None

    if num_elements == n:
        return head.next

    counter = 0
    prev = head
    cur = head.next
    while counter < num_elements - n - 1:
        if prev is not None:
            prev = prev.next
        if cur is not None:
            cur = cur.next

        counter += 1
    if cur is not None and prev is not None:
        prev.next = cur.next
    elif prev is not None:
        prev.next = None
    return head
