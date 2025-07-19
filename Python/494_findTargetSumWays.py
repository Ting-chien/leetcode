from typing import List
from functools import cache
import collections


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


class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cnt = 0 # 紀錄有多少組算式總和為 target
        # 透過 DFS 遞迴計算所有可能的算式
        def dfs(idx: int, curr: int):
            """
            Args:
                idx: 當前遞迴的 index
                curr: 當前累積的總和
            """
            if idx == len(nums):
                if curr == target:
                    nonlocal cnt
                    cnt += 1
                return
            # 遞迴計算所有可能的算式
            dfs(idx+1, curr+nums[idx])
            dfs(idx+1, curr-nums[idx])
        dfs(0, 0)
        return cnt
    

class Solution4:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(2^N)
        Space Complexity: O(N)
        """
        # 改寫 Solution3 的方法，直接在 DFS 遞迴中相加選 + 或選 - 的結果
        def dfs(idx: int, curr: int):
            """
            Args:
                idx: 當前遞迴的 index
                curr: 當前累積的總和
            """
            if idx == len(nums):
                return 1 if curr == target else 0
            # 遞迴計算所有可能的算式
            return dfs(idx+1, curr+nums[idx]) + dfs(idx+1, curr-nums[idx])
        return dfs(0, 0)
    

class Solution5:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(N*sum(nums))
        Space Complexity: O(N*sum(nums))
        """
        # 原本 Solution4 的方法會超時，因此透過一二維陣列來儲存已經計算過的結果
        # memo[i][j] 代表 nums 前 i 個數字的總和為 j 的組合數
        memo = [[-1] * (2*sum(nums)+1) for _ in range(len(nums))]
        # 透過 DFS 遞迴計算所有可能的算式
        def dfs(idx: int, curr: int):
            """
            Args:
                idx: 當前遞迴的 index
                curr: 當前累積的總和
            """
            if idx == len(nums):
                if curr == target:
                    return 1
                return 0
            if memo[idx][curr] != -1:
                return memo[idx][curr]
            # 遞迴計算所有可能的算式
            memo[idx][curr] = dfs(idx+1, curr+nums[idx]) + dfs(idx+1, curr-nums[idx])
            return memo[idx][curr]
        return dfs(0, 0)
    

class Solution6:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """還未寫完"""
        # 透過二維的 dp 來儲存所有可能的組合數
        dp = [[0] * (2*sum(nums)+1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for j, cnt in enumerate(dp[i]):
                print(f"i={i}, j={j}, cnt={cnt}")
                dp[i+1][j+num] += cnt
                dp[i+1][j-num] += cnt
        return dp[len(nums)][target]

class Solution7:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Memorization"""
        # make sure our target is calculable
        target += sum(nums)
        if target < 0 or target % 2 != 0: return 0
        target = target // 2
        # calculate how many type can be select
        memo = [[-1] * (target+1) for _ in range(len(nums))]
        def dfs(i, t):
            """
            :param i: Number of integer to be select
            :param t: Target need to met
            """
            # if no remain integer
            if i < 0:
                return 1 if t == 0 else 0
            # if answer is memorized
            if memo[i][t] != -1:
                return memo[i][t]
            # return if the number can not be chosen
            if nums[i] > t:
                return dfs(i-1, t)
            # decide to select or not
            ans = dfs(i-1, t) + dfs(i-1, t-nums[i])
            memo[i][t] = ans
            return ans
        return dfs(len(nums)-1, target)
        

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
res = Solution7().findTargetSumWays(nums = [1,1,1,1,1], target = 3)
print(res)

# Example 2:
# Input: nums = [1], target = 1
# Output: 1
res = Solution7().findTargetSumWays(nums = [1], target = 1)
print(res)