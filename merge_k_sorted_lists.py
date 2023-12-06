import typing as t
from reverse_linked_list import ListNode

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""


def mergeKLists(lists: t.List[t.Optional[ListNode]]) -> t.Optional[ListNode]:
    """_summary_
    Algorithm:
    1. Prune lists to non None. We don't have to do this but is easy, and
    while O(n) storage, is a list of pointers making it lightweight.
    2. Early exit for base case
    3. Initialize head and cur
    4. Loop through nodes and find minimum; O(n)/O(1)
    5. Increment list containing minimum, prune if necessary.
    6. Create list of unexhausted lists. You don't need this, but it saves hitting Nones every single time at the cost
        of a tiny bit of memory. List of pointers is small; O()/O(n)
    7. Additionally initialize counter of remaining ListNode's to consume
    8. While we have lists remaining: O(sum of lengths of ListNodes) or in equal length lists, O(n*m^2).
        If you use a heap, mlogm but you cost memory. Basically we can tweak this to be constant memory,
        or use a heap to get better performance
    8b. Loop to get the minimum but only check unexhausted lists O(# lists = m)
    8c. increment our new ListNode
    8d. Increment the list we took its node from
    8e. If we finished a list, decrement remasining lists and remove from consideration.
    9. Return result

    Args:
        lists (t.List[t.Optional[ListNode]]): List of Listnodes in sorted order to merge

    Returns:
        t.Optional[ListNode]: Combined sorted list of ListNodes
    """
    pruned_lists: list[ListNode] | None = [x for x in lists if x is not None]
    if len(pruned_lists) == 0:
        return None

    # get minimum head
    head: ListNode = pruned_lists[0]
    cur = head
    head_idx = 0
    for i, list_node in enumerate(pruned_lists):
        if list_node.val < head.val:
            head = list_node
            head_idx = i
    # increment head to prevent duplicate
    # This one sucks because it works, but I can't get the typing of pruned_lists
    # correct with all the other code so we abuse type: ignore as hatch to avoid
    # refactoring this entire code. In code review/prod this would/should be reviewed
    # a bit more.
    pruned_lists[head_idx] = pruned_lists[head_idx].next
    if t.cast(ListNode | None, pruned_lists[head_idx]) is None:
        pruned_lists.pop(head_idx)

    # this will be storage of which listNodes aren't none. This allows us to skip over None's so if
    # one list is say 1 billion long, and the other are one long, we aren't a billion times checking all of the others
    unexhausted_lists = list(range(len(pruned_lists)))
    remaining_lists = len(
        pruned_lists
    )  # when this hits 0 all are exhausted. Means we don't have to for each cycle recalculate from scratch
    while remaining_lists != 0:
        minimum_guess = pruned_lists[unexhausted_lists[0]]
        min_idx = unexhausted_lists[0]
        # get minimum
        for idx in unexhausted_lists[1:]:
            if pruned_lists[idx].val < minimum_guess.val:
                minimum_guess = pruned_lists[idx]
                min_idx = idx
        # add to sorted list
        cur.next = minimum_guess
        cur = cur.next
        # increment minimum list
        # same as above
        pruned_lists[min_idx] = pruned_lists[min_idx].next  # type: ignore
        # handle None, removing it from options
        if t.cast(ListNode | None, pruned_lists[min_idx]) is None:
            remaining_lists -= 1
            unexhausted_lists.pop(unexhausted_lists.index(min_idx))
    return head
