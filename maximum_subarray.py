import typing as t

"""
Given an integer array nums, find the 
subarray
with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explnation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
# TODO


def maxSubArray(nums: t.List[int]) -> int:
    """We determine the biggest sum of a subarray, e.g. a contiguous block. We do this in a two pass solution.
    Algorithm: O(n)/O(n)
    1. Pass 1, for each element if we are in a positive run sum and replace to positives w/ indicies (touple of sum, start, end), if we are in a negative run, sum and replace into a negative single value; O(n)/O(1)
    2. Trim first and last if they are negative
    2. Now the array is just alternating positives and negatives. Pass 2, start with and only add n+1 and n+2 if n+2>n+1. If n > n+2, iterate forward keeping track of "best score". Else, n+2 is now best score.


    Args:
        nums (t.List[int]): _description_

    Returns:
        int: _description_
    """

    if len(nums) == 0:
        raise ValueError
    if len(nums) == 1:
        return nums[0]
    return 0

    # if len(nums) == 0:
    #     return 0

    # if len(nums) == 1:
    #     return nums[0]

    # condensed_arr: t.List[t.Tuple[int, int, int]] = []
    # positive_streak = nums[0] >= 0
    # current_sum = nums[0]
    # streak_start: int = 0
    # for i, elem in enumerate(nums[1:], 1):
    #     # if our current streak continues
    #     if elem == 0 or (positive_streak is (elem > 0)):
    #         current_sum += elem
    #     # wrap up current streak
    #     else:
    #         condensed_arr.append((current_sum, streak_start, i - 1))
    #         streak_start = i
    #         current_sum = elem
    #         positive_streak = elem > 0
    # condensed_arr.append((current_sum, streak_start, len(nums) - 1))
    # # [1, 2, -1, -2, 3, 4] is now formatted as [(sub array sum, sub array start, sub array end), ...]
    # # [(3, 0, 1), (-3, 2, 3), (7, 4, 5)]

    # if len(condensed_arr) == 1 and condensed_arr[0][0] <= 0:
    #     return max(nums)
    # elif len(condensed_arr) == 1 and condensed_arr[0][0] > 0:
    #     return sum(nums)

    # # trim so ends are always positive
    # if condensed_arr[0][0] < 0:
    #     condensed_arr = condensed_arr[1:]
    # if len(condensed_arr) > 0 and condensed_arr[-1][0] < 0:
    #     condensed_arr = condensed_arr[:-1]

    # if len(condensed_arr) == 0:
    #     return 0
    # if len(condensed_arr) == 1:
    #     return condensed_arr[0][0]

    # # [pos, neg, pos, neg, pos]
    # while len(condensed_arr) > 4:  # each iter reduces length by 2, O(n)
    #     if condensed_arr[0][0] + condensed_arr[1][0] <= 0:
    #         condensed_arr = condensed_arr[2:]
    #     else:
    #         # [BiggerPos, neg, pos]
    #         condensed_arr = [
    #             (
    #                 condensed_arr[0][0] + condensed_arr[1][0] + condensed_arr[2][0],
    #                 condensed_arr[0][1],
    #                 condensed_arr[2][2],
    #             ),
    #             *condensed_arr[3:],
    #         ]
    # if len(condensed_arr) == 3:
    #     # [pos, neg, pos]
    #     if (
    #         condensed_arr[1][0] + condensed_arr[0][0] >= 0
    #         and condensed_arr[1][0] + condensed_arr[2][0] >= 0
    #     ):
    #         return condensed_arr[0][0] + condensed_arr[1][0] + condensed_arr[2][0]
    #     return (
    #         condensed_arr[0][0]
    #         if condensed_arr[0][0] > condensed_arr[2][0]
    #         else condensed_arr[2][0]
    #     )
    # raise ValueError(f"err! {condensed_arr}")
