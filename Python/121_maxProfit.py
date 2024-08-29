from typing import List


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        buying = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # get temporary max profit 
            selling = prices[i]
            profit = max(profit, selling-buying)
            # find lower buying price
            if selling < buying:
                buying = selling
        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # 定義當前獲利為0，且最低股價為正無限大
        res, curr_min = 0, float('inf')
        # 接著遍歷所有日期的股價，並計算股票價差。若大於最大
        # 獲利則更新res，若有更低的股價則更新curr_min（重新買入）
        for p in prices:
            res = max(res, p-curr_min)
            curr_min = min(p, curr_min)
        return res
    

print(Solution2().maxProfit([7,1,5,3,6,4]))
print(Solution2().maxProfit([7,6,4,3,1]))