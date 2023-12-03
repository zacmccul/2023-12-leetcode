import typing as t

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


def maxProfit(prices: t.List[int]) -> int:
    """
    Determines max profit from sequential list of price points.
    We have array of prices in sequential time. We want max(i-j) where i<j
    Algorithm:
    1. Create left/right iter at beginning 0,1; O(1)/O(1)
    2. While right < len(prices): O(n)/O(1)
        2a. get potential profit of our current iters O(1)/O(1)
        2b. If potential is negative, we have already checked each previous profit comparison. So we only need to check future ones, but this price is lower than our left comparison, meaning it'll always be a greater profit to any future price we compare to, so we can just set our left iter (our base) to this point
        2c. Else, check if this profit is bigger than max and save. O(1)/O(1)
        2d. Increment right to check next potential profit O(1)/O(1)


    Args:
        prices (t.List[int]): List of integer price points

    Returns:
        int: Max potential profit, or minimum of 0.
    """
    max_profit = 0
    left = 0
    right = 1
    while right < len(prices):
        potential_prof = prices[right] - prices[left]

        if potential_prof < 0:
            left = right
        else:
            max_profit = max(max_profit, potential_prof)
        right += 1
    return max_profit

    # hash_map = {k: v for v, k in enumerate(prices)}
    # prices.sort()
    # min_iter, max_iter = 0, len(prices) - 1
    # min_val, max_val = prices[0], prices[max_iter]
    # while min_iter < max_iter:
    #     if hash_map[min_val] < hash_map[max_val]:
    #         return max_val - min_val
    #     # now get next smallest potential profit margin
    #     min_increment_sum = prices[max_iter] - prices[min_iter + 1]
    #     max_increment_sum = prices[max_iter - 1] - prices[min_iter]
    #     if max_increment_sum > min_increment_sum:
    #         max_iter -= 1
    #         max_val = prices[max_iter]
    #     else:
    #         min_iter += 1
    #         min_val = prices[min_iter]
