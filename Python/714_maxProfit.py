from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        利用兩條 dp 陣列去儲存持有股票(獲利)、賣出股票(手上現金)的最大獲利，
        1. 持有股票 hold => hold[i] = max(hold[i-1], cash[i-1]+prices[i])
        2. 賣出股票 cash => cash[i] = max(cash[i-1], prices[i]+hold[i-1]-fee)

        Complexity
        * Time: O(n) - beats 53.10%
        * Space: O(n) - beats 45.06%
        """
        n = len(prices)
        hold = [0] * n
        cash = [0] * n
        
        hold[0] = -prices[0]  # 第 0 天買股票
        cash[0] = 0           # 第 0 天不持股
        
        for i in range(1, n):
            hold[i] = max(hold[i-1], cash[i-1] - prices[i])
            cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
        
        return cash[-1]