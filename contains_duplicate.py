import typing as t

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


def containsDuplicate(nums: t.List[int]) -> bool:
    """Determines if there are duplicate elements in the arr. Good approach if space in the average case isn't a concern

    Args:
        nums (t.list[int]): The input list of nums

    Returns:
        bool: True if it contains duplicates
    """
    return len(nums) != len(set(nums))
