from typing import List
from functools import cache


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i: int, amount: int):
            """
            :param i: Number of items to be select
            :param amount: Left capacity of backpack
            """
            # no item to choose
            if i < 0:
                return 0 if amount == 0 else float('inf')
            # no capacity 
            if coins[i] > amount:
                return dfs(i-1, amount)
            # decide to select or not
            return min(dfs(i-1, amount), dfs(i, amount-coins[i])+1)
        res = dfs(len(coins)-1, amount)
        return res if res < float('inf') else -1
    

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # 定義邊界條件
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        dp[0][0] = 0
        # 遍歷所有錢幣和金額的最小組成方式
        for i in range(n):
            for a in range(amount+1):
                if coins[i] > a:
                    dp[i+1][a] = dp[i][a]
                else:
                    dp[i+1][a] = min(dp[i][a], dp[i+1][a-coins[i]]+1)
        res = dp[n][amount]
        return res if res < float('inf') else -1