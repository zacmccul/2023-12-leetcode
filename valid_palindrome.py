# import typing as t

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def isPalindrome(s: str) -> bool:
    """Determines if string, when ignoring non alphanum characters, is palindromic. O(n)/O(1)
    Algorithm:
    1. Build iterator to traverse a lowered alphanum only version of s; O(1)/O(1)
    2. Build a reverse iterator to do the same as 1. O(1)/O(1)
    3. Iterate over each iterator together ensuring they are equal O(n/2)/O(1)

    Args:
        s (str): _description_

    Returns:
        bool: _description_
    """
    forward_gen = (
        c.lower() for c in s if c.isalnum()
    )  # O(1)/O(1) Generators are constant memory
    backward_gen = (
        s[i].lower() for i in range(len(s) - 1, -1, -1) if s[i].isalnum()
    )  # O(1)/O(1) could also use reversed

    # All checks if each element in it is true. It is very very fast combined with generators.
    # We are not creating a list here, rather it's being consumed piecewise.
    # So O(s//2) iterations with constant memory.
    # don't need to check middle character b/c palindrome is looking for equal to itself
    return all(
        next(forward_gen, True) == next(backward_gen, True) for _ in range(len(s) // 2)
    )
