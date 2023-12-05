import typing as t
from reverse_linked_list import ListNode

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""


def hasCycle(head: t.Optional[ListNode]) -> bool:
    """I looked it up and this is apparently standard approach, but I swear I've never seen this before.
        Uses fast and slow pointer, if fast pointer his the end, no cycle. If fast pointer hits the slow pointer, cycle.
        Think cars and traffic
    Algorithm: O(n)/O(1)
    1. If head is None return None O(1)
    2. Initialize two pointers, one slow one fast.
    3. Loop while fast pointer is not None, e.g. not at end of listnode
    3a. Increment fast pointer by one
    3b. Check if we have any exit conditions (fast pionter hit end of list or fast pointer hit slow pointer)
    3c. Increment fast and slow by one.
    3d. Check exit conditions again
    4. Out of loop just check exit conditiosn again and return.


    Args:
        head (t.Optional[ListNode]): _description_

    Returns:
        bool: _description_
    """
    if head is None:
        return False
    slow_ptr: ListNode | None = head
    fast_ptr: ListNode | None = head
    while fast_ptr is not None:
        fast_ptr = fast_ptr.next
        if fast_ptr is None or slow_ptr is None:
            return False
        elif fast_ptr is slow_ptr:
            return True
        fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next
        if fast_ptr is slow_ptr:
            return True
    if fast_ptr is None:
        return False
    return slow_ptr is fast_ptr
