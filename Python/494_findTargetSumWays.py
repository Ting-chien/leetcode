from typing import List
from functools import cache


def zero_one_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    @cache
    def dfs(i: int, cap: int):
        """
        :param i: Number of items to be select
        :param cap: Left capacity of backpack
        """
        # no item to choose
        if i < 0:
            return 0
        # no capacity 
        if wgt[i] > cap:
            return dfs(i-1, cap)
        # decide to select or not
        return max(dfs(i-1, cap), dfs(i-1, cap-wgt[i])+val[i])
    return dfs(len(wgt)-1, capacity)

res = zero_one_knapsack(capacity=50, wgt=[10,20,30,40,50], val=[50,120,150,210,240])
print(res)


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # make sure our target is calculable
        target += sum(nums)
        if target < 0 or target % 2 != 0: return 0
        target = target // 2
        # calculate how many type can be select
        @cache
        def dfs(i, t):
            """
            :param i: Number of integer to be select
            :param t: Target need to met
            """
            # if no remain integer
            if i < 0:
                return 1 if t == 0 else 0
            # return if the number can not be chosen
            if nums[i] > t:
                return dfs(i-1, t)
            # decide to select or not
            return dfs(i-1, t) + dfs(i-1, t-nums[i])
        return dfs(len(nums)-1, target)
    

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # make sure our target is calculable
        target += sum(nums)
        if target < 0 or target % 2 != 0: return 0
        target = target // 2
        # calculate how many type can be select
        n = len(nums)
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1 # only one solution for zero items with targe=0
        for i in range(n):
            for t in range(target+1):
                if t < nums[i]:
                    dp[i+1][t] = dp[i][t]
                else:
                    dp[i+1][t] = dp[i][t] + dp[i][t-nums[i]]
        return dp[n][target]
    

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
res = Solution2().findTargetSumWays(nums = [1,1,1,1,1], target = 3)
print(res)

# Example 2:
# Input: nums = [1], target = 1
# Output: 1
res = Solution2().findTargetSumWays(nums = [1], target = 1)
print(res)