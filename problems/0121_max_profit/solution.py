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
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # 第一天獲利必為 0
        min_price = prices[0] # 第一天可以得到的最小股價必為自身價錢
        for p in prices[1:]:
            min_price = min(min_price, p) # 比較誰才是歷史最低股價
            max_profit = max(max_profit, p - min_price) # 比比看是否能從 p - min_price 得到更高獲利
        return min_price
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            cash = max(cash, hold+p) # 不賣 vs 賣出
            hold = max(hold, -p) # 每次買入都是最低價
        return cash
    

print(Solution2().maxProfit([7,1,5,3,6,4]))
print(Solution2().maxProfit([7,6,4,3,1]))