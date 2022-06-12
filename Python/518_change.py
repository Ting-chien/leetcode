from itertools import count
from typing import Dict, List

class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Clean up the coins list with sorted and smaller than amount
        coins = list(filter(lambda x: x <= amount, sorted(coins)))
        return self.recursion(amount, coins)
        
    def recursion(self, remain: int, coins: List[int]) -> int:

        # If remain is 0
        if remain == 0: return 1

        # If remain is not 0
        if len(coins) == 0: return 0
        if len(coins) == 1: return 1 if remain % coins[0] == 0 else 0

        # Try with different permutations
        result, count = 0, 0
        tail_coin, remain_coins = coins[-1], coins[:-1]
        while count*tail_coin <= remain:
            result += self.recursion(remain-count*tail_coin, remain_coins)
            count += 1

        return result

class Solution2:
    '''比上一個方法好的地方是，透過dict來儲存之前已計算過的資訊'''
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Clean up the coins list with sorted and smaller than amount
        coins = list(filter(lambda x: x <= amount, sorted(coins)))
        cache = {}
        return self.recursion(amount, coins, cache)
        
    def recursion(self, remain: int, coins: List[int], cache) -> int:

        # If remain is 0
        if remain == 0: return 1

        # If remain is not 0
        if len(coins) == 0: return 0
        if len(coins) == 1: return 1 if remain % coins[0] == 0 else 0

        # Return if the combination has been calculated
        key = "{}|{}".format(remain, ",".join([str(x) for x in coins]))
        if key in cache: return cache[key]

        # Try with different permutations
        result, count = 0, 0
        tail_coin, remain_coins = coins[-1], coins[:-1]
        while count*tail_coin <= remain:
            result += self.recursion(remain-count*tail_coin, remain_coins, cache)
            count += 1

        cache[key] = result

        return result

class Solution2:
    '''對所有可組成目標面額的幣值做遍歷，dp[i]的解決方案為dp[i]+dp[i-coin]'''
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]

if __name__ == '__main__':
    sol = Solution2()
    # print(sol.change(5, [1,2,5]))
    # print(sol.change(3, [2]))
    # print(sol.change(10, [10]))
    print(sol.change(500, [1,2,5]))