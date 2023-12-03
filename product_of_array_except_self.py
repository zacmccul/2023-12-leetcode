import typing as t

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


def productExceptSelf(nums: t.List[int]) -> t.List[int]:
    """Modify in place input nums to be product of every number other than itself
    Algorithm: We need to multiply any given ith position with all of the other numbers.
    We can do this in two passes, the first by building up a composite number of the product of all the numbers prior to i, incrementing
    and then going backwards by building up a composite number of the product of all numbers after i decrement. Because multiplication is commutative
    this means we effectively multiply *each* i by product(prior numbers to i) * product(post numbers to i) = product(all numbers not i)
    1. Create precomposite, postcomposite, set both equal to 1; O(1)
    2. For each num in nums not i; O(n)/O(1)
    1a. nums[i] *= precomposite; O(1)/O(1)
    1b. precomposite = nums[i]; O(1)/O(1)
    3. For each num in nums no i reversed;
    3a. nums[i] *= postcomposite;
    3b. postcomposite = nums[i]
    return nums

    Args:
        nums (t.List[int]): Input num array to modify

    Returns:
        t.List[int]: Outputted product'ized array
    """
    new_nums = [1] * len(nums)
    pre_composite, post_composite = 1, 1
    for i in range(len(nums)):
        new_nums[i] *= pre_composite
        pre_composite *= nums[i]
    # reverse iterate
    for j in range(len(nums) - 1, -1, -1):
        new_nums[j] *= post_composite
        post_composite *= nums[j]
    return new_nums
