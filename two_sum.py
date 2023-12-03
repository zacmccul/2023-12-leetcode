import typing as t

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


def twoSum(nums: t.List[int], target: int) -> t.List[int]:
    """
    Time: nlogn
    Space: n
    Algorithm:
        1. We sort for nlogn into new array (n space )
        2. we have two pointers, one on min one on max and then we track their sum
        3. if their sum is too large, max goes down
        4. if their sum is too small, min goes up
        Steps 3. and 4. are looped, and as each step they move to each other, this can only run at most n times
        So we nlogn steps to sort, then n steps,
        5. Get the indicies from our unsorted (happens at most 2n times)
        6. If indicies are different, we're done c
        7. If they are the same, then we pop from nums and get the "next index" which is at most n-1 steps
        8. return


    Args:
        nums (t.List[int]): The input array of candidates
        target (int): The sum we need to sum to

    Returns:
        t.List[int]: Two element list of the indicies from lowest to highest corresponding to numbers in nums that sum to the target.
    """
    # sort + setup initial vars
    sorted_nums = sorted([*nums])
    min_i = 0
    max_i = len(sorted_nums) - 1
    iters = 0

    # easy func to get the latest sum with the new min/max indicies
    def get_sum(x: int, y: int) -> int:
        return sorted_nums[x] + sorted_nums[y]

    cur_sum = get_sum(min_i, max_i)

    # keep going until we match our target OR hit max iter
    while cur_sum != target and iters < 10_000:
        # if our sum is too small, make the next sum larger (guaranteed b/c sorted)
        if cur_sum < target:
            min_i += 1
        # same but make the next sum smaller
        elif cur_sum > target:
            max_i -= 1
        iters += 1
        cur_sum = get_sum(min_i, max_i)
    if iters == 10_000:
        raise ValueError("Iterated for 10,000 cycles and did not find an answer!")
    # error handling in case algo fails
    elif min_i >= len(nums) or max_i < 0:
        raise ValueError(f"Min and max went to bad places {min_i} with max: {max_i}")

    # translate sorted indicies into original nums indicies
    indicies = [nums.index(sorted_nums[min_i]), nums.index(sorted_nums[max_i])]
    # handle case if our sum is made from two identical numbers, can't return same index twice
    if indicies[0] == indicies[1]:
        nums.pop(indicies[0])
        indicies[1] = nums.index(sorted_nums[max_i]) + 1
    return indicies
