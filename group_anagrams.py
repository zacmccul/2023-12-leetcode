import typing as t

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


def groupAnagrams(strs: t.List[str]) -> t.List[t.List[str]]:
    """A great *scaling* solution to big big strings, but slow in the realistic case. O(m*n), where m is # of strings,
        and n is length of a string, with O(m) space.
    Algorithm:
    1. Define hashize which turns string into 26 length dictionary of frequency count of characters.
        Each dict is sorted alphabetically.
    2. For each word loop:
    2a. Calculate hashed version O(n)/O(c)
    2b. Turn the dict into a string so we can hash it as a key; O(c)/O(c). Since frequency dict is always length 26, the
        hashed version is simiarly fixed length.
    2c. Use this hashable version as a key, to store in our output with the word as a value.
        This means any two words which are anagrams have a common representation that is hashable.
        Essentially we've created a transformation that maps all anagrams of a word in length of the word time to one
        output allowing us to then just "check" each word and store them together.
    3. Convert the values to a list and return, which in the worst case is m iterations.

    Args:
        strs (t.List[str]): _description_

    Returns:
        t.List[t.List[str]]: _description_
    """
    abc = "abcdefghijklmnopqrstuvwxyz"

    def hashize(inp: str) -> dict[str, int]:
        """Given an input string turns it into a count of each char in a dict. One pass O(n)/O(n)

        Args:
            inp (str): The input string

        Returns:
            dict[str, int]: Dict mapping a unique char in inp to # of occurences
        """

        out: dict[str, int] = {k: 0 for k in abc}  # O(1)
        for char in inp:  # O(n)
            out[char] += 1
        return out

    frequency_list: dict[str, list[str]] = {}
    for word in strs:  # m loops, one for each string in strs
        frequency_dict = hashize(word)  # iterate over each char in a word
        hashable_freq = ";".join(
            f"{k}:{v}" for k, v in frequency_dict.items()
        )  # 26 iterations, constant space
        if hashable_freq not in frequency_list:  # o(1)
            frequency_list[hashable_freq] = [word]
        else:
            frequency_list[hashable_freq].append(word)  # O(c)
    return list(frequency_list.values())  # O(m)
