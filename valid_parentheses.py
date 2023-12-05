"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def isValid(s: str) -> bool:
    """Verifies if parentheses are correct. O(n)/O(n).
    Algorithm:
    1. Initialize inital stack to empty arr and define open/closed parens. O(1)/O(1)
    2. Loop through each char in s: O(n)/O(n)
    2a. If we have an open parentheses, append to stack. O(1)/O(1)
    2b. Else if we have a closed paren:
    2c. If stack is empty, we have closed without corresponding open. Return False
    2d. Get the corresponding closing paren O(1)/O(1)
    2e. If we have the right closing paren on top of stack, remove that from the stack.
    2f. If we don't, invalid and return False.
    2g. Only return true if our stack is empty, i.e. every parenthese has been matched correctly.

    Args:
        s (str): The input string.

    Returns:
        bool: True if parentheses are valid, false otherwise.
    """

    open_parens = "([{"
    closed_parens = ")]}"

    stack: list[str] = []

    for char in s:
        if char in open_parens:
            stack.append(char)
        elif char in closed_parens:
            if len(stack) == 0:
                return False
            compliment = open_parens[closed_parens.index(char)]
            if compliment == stack[-1]:
                stack = stack[:-1]
            else:
                return False
    return len(stack) == 0
