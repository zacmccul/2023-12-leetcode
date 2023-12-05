"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def isAnagram(s: str, t: str) -> bool:
    """Verifies if s and t are anagrams of each other. O(n) storage, O(n) time, two pass approach.
    Algorithm:
    1. Initialize hash map & get length: O(1)/O(1)
    2. Loop for each char in s: O(1)/O(s)
    2a. If char not in hash map, add it and map to 1; O(1)/O(1)
    2b. If char in hash map, add 1; O(1)/O(1)
    3. Loop for each char in t:
    3a. If char not in hash map, return False; O(1)/O(1)
    3b. Subtract 1 from hash map, decrement length tracker
    3c. If we get negative, then t has more of that char than s, meaning not an anagram. Return false;
    4. Return if we used the exact same number of letters


    Args:
        s (str): An input string
        t (str): An input string

    Returns:
        bool: If s and t are anagrams.
    """

    break_down: dict[str, int] = {}
    break_down_sum = len(s)
    for char in s:
        if char not in break_down:
            break_down[char] = 1
        else:
            break_down[char] += 1

    for char in t:
        if char not in break_down:
            return False
        break_down[char] -= 1
        break_down_sum -= 1
        if break_down[char] < 0:
            return False
    return break_down_sum == 0
