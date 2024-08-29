from typing import List


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """
        透過雙指針遍歷整個list，若當日的股票價格低於前一日，
        則回到前一日把股票出清，並衝新買入當日價格的股票。
        """
        # if no profit is available
        if len(prices) <= 1: return 0

        # initialize start buying point
        l_p, r_p = 0, 1
        profit = 0
        
        # main
        while r_p < len(prices):
            # selling and rebuy if today's price is lower than yesterday
            if prices[r_p] < prices[r_p-1]:
                # gain profit if selling price higher than buying price
                buying = prices[l_p]
                selling = prices[r_p-1]
                if selling > buying:
                    print(f"Buy at {buying} and sell at {selling}")
                    profit += selling-buying
                # rebuy
                l_p = r_p
            # check the last day
            elif r_p == len(prices)-1:
                buying = prices[l_p]
                selling = prices[r_p]
                if selling > buying:
                    print(f"Buy at {buying} and sell at {selling}")
                    profit += selling-buying
            # to next day
            r_p += 1

        return profit
    

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

print(Solution2().maxProfit([7,1,5,3,6,4]))
print(Solution2().maxProfit([1,2,3,4,5]))
print(Solution2().maxProfit([7,6,4,3,1]))