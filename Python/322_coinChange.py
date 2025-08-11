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
    

class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # 定義邊界條件(當 coin=0 時，不管 amount 多少都是 inf)
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        # 當 amount=0 時，不管 coin 多少都是 0
        for i in range(n+1):
            dp[i][0] = 0
        # 遍歷所有錢幣和金額的最小組成方式
        for i in range(1, n+1):
            for a in range(1, amount+1):
                if coins[i-1] > a:
                    dp[i][a] = dp[i-1][a]
                else:
                    dp[i][a] = min(dp[i-1][a], dp[i][a-coins[i-1]]+1)
        res = dp[n][amount]
        return res if res < float('inf') else -1
    

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
res = Solution3().coinChange(coins = [1,2,5], amount = 11)
print(res)

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
res = Solution3().coinChange(coins = [2], amount = 3)
print(res)