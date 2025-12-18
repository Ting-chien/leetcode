from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Use rest, sell, hold to represent states of not buying,
        sold, and hold the stock.
        """

        # Initial states (day 1)
        n = len(prices)
        rest, hold, sell = [0] * n, [0] * n, [0] * n
        hold[0] = -prices[0]

        # Start from day 2
        for i in range(1, n):
            rest[i] = max(rest[i-1], sell[i-1])
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sell[i] = max(sell[i-1], prices[i] + hold[i-1])

        # Return max of state with no stock on hand
        return max(rest[-1], sell[-1])
    

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
print(Solution().maxProfit(prices = [1,2,3,0,2]))