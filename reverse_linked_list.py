import copy
import typing as t

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.


"""


class ListNode:
    def __init__(self, arr: list[int]) -> None:
        if len(arr) == 0:
            self.val = None
            self.next = None
        else:
            self.val = arr.pop(0)
            self.next = ListNode(arr) if len(arr) else None

    def __repr__(self) -> str:
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} -> {repr(self.next)}"


def reverseList(head: t.Optional[ListNode]) -> t.Optional[ListNode]:
    """Test function to ensure that different implementations match for testing.

    Args:
        head (t.Optional[ListNode]): The input ListNode that can be copied to verify.

    Returns:
        t.Optional[ListNode]: Picks arbitrarily one output to return, but they are asserted to all be identical first.
    """
    to_output = reverseList_list(copy.deepcopy(head))
    outputs = [
        reverseList_list(copy.deepcopy(head)),
        reverseList_pointers(copy.deepcopy(head)),
        reverseList_pointers_recursive(copy.deepcopy(head)),
    ]
    assert len(set(str(x) for x in outputs)) == 1

    return to_output


def reverseList_pointers_recursive(head: t.Optional[ListNode]) -> t.Optional[ListNode]:
    """Using pointer chasing, reverse a singly linked list *recursively*.
    Algorithm: (Using [1,2,3,4] as example)
    1. If head is none return none
    2. Initialize two pointers, one to the head which is cur (1), which represents the first node
        the second is cur_next (2) which is the one that needs to be pointed backwards.
        We will need to save its next value before overriding it.
        Additionally set cur.next to None as it is now the tail
    3. Instead of looping we define our recursion function to take in the cur_node and next node
    3a. Base case of if next is None, return cur_node. This is just like our while loop stop condition.
    3b. Save cur_next.next (3)
    3c. Set cur_next.next to point to cur (2) -> (1)
    3d. cur (1) set to cur_next (2)
    3e. cur_next (2) set to temp (3)
    3f. Recurse to work on the next set of nodes, returning the result. This will return reversed list.
    Args:
        head (t.Optional[ListNode]): An input linked list or None

    Returns:
        t.Optional[ListNode]: The reverse linked list, or None if head is None.
    """
    if head is None:
        return None
    cur = head
    cur_next = head.next
    cur.next = None

    def recurse(cur_node: ListNode, cur_next_node: ListNode | None) -> ListNode:
        if cur_next_node is None:
            return cur_node
        temp = cur_next_node.next
        # set next node to point backwards to cur
        cur_next_node.next = cur_node
        # cur is incremented one
        cur_node = cur_next_node
        # cur_next is incremented one
        cur_next_node = temp
        return recurse(cur_node, cur_next_node)

    return recurse(cur, cur_next)


def reverseList_pointers(head: t.Optional[ListNode]) -> t.Optional[ListNode]:
    """Using pointer chasing, reverse a singly linked list.
    Algorithm: (Using [1,2,3,4] as example)
    1. If head is none return none
    2. Initialize two pointers, one to the head which is cur (1), which represents the first node
        the second is cur_next (2) which is the one that needs to be pointed backwards.
        We will need to save its next value before overriding it.
        Additionally set cur.next to None as it is now the tail
    3. Loop until cur_next is None; O(n)/O(1)
    3a. Save cur_next.next (3)
    3b. Set cur_next.next to point to cur (2) -> (1)
    3c. cur (1) set to cur_next (2)
    3d. cur_next (2) set to temp (3)
    4. Return our reversed list
    Args:
        head (t.Optional[ListNode]): An input linked list or None

    Returns:
        t.Optional[ListNode]: The reverse linked list, or None if head is None.
    """
    if head is None:
        return None
    cur = head
    cur_next = head.next
    cur.next = None
    while cur_next is not None:
        # grab next node
        temp = cur_next.next
        # set next node to point backwards to cur
        cur_next.next = cur
        # cur is incremented one
        cur = cur_next
        # cur_next is incremented one
        cur_next = temp
    # we have reached the end
    return cur


def reverseList_list(head: t.Optional[ListNode]) -> t.Optional[ListNode]:
    """Using a traversal list of pointers, reverses the order of a singly linked list.
        Usually faster than pointer chasing at the cost of tiny bit of memory and the spirit of the challenge.
    Algorithm: O(n)/O(n) (but storage is list of pointers, not the value itself)
    1. If head is None return None
    2. Initialize traversal list
    3. Loop: O(n)/O(n)
    3a. Store each node pointer in list
    4. Finish storing the list and grab the tail
    5. In reverse order traverse using the list and swap directiosn of each node.
    6. Return the old tail which is the new head.

    Args:
        head (t.Optional[ListNode]): An input linked list or None

    Returns:
        t.Optional[ListNode]: The reverse linked list, or None if head is None.
    """
    if head is None:
        return None
    traversal_list: list[ListNode] = []
    while head.next is not None:
        traversal_list.append(head)
        head = head.next
    traversal_list.append(head)
    tail = traversal_list[-1]
    iterator: ListNode = tail
    for item in reversed(traversal_list):
        iterator.next = item
        iterator = item
    iterator.next = None
    return tail
