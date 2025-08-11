from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Limit Exceeded
        """
        def dfs(n):
            # if no house to rob
            if n < 0:
                return 0
            # else, compare robbing n-1th or n-2th house
            return max(dfs(n-1), dfs(n-2)+nums[n])
        return dfs(len(nums)-1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Limit Exceeded
        """
        memo = [None] * (len(nums)+1)
        def dfs(i: int):
            if i == 0:
                return 0
            if i == 1:
                return nums[i-1]
            if not memo[i]:
                memo[i] = max(dfs(i-1), dfs(i-2)+nums[i-1])
            return memo[i]
        return dfs(len(nums))
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Bottom-up DP
        
        Complexity
        * Time: O(n) - beats 100%
        * Space: O(n) - beats 85.52%
        """
        memo = [0] * (len(nums)+1)
        memo[0], memo[1] = 0, nums[0]
        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i]+memo[i-1], memo[i])
        return memo[len(nums)]

# class Solution2:
#     def rob(self, nums: List[int]) -> int:
#         """
#         Use cache to prevent calculate repetely
#         Time: O(n)
#         Space: O(n)
#         """
#         cache = [-1] * len(nums)
#         def dfs(n):
#             """
#             :param n: Number of house remain to be robbed
#             """
#             # if no house to rob
#             if n < 0:
#                 return 0
#             # else, compare robbing n-1th or n-2th house
#             if cache[n] != -1:
#                 return cache[n]
#             res = max(dfs(n-1), dfs(n-2)+nums[n])
#             return res
#         return dfs(len(nums)-1)
    

# class Solution3:
#     def rob(self, nums: List[int]) -> int:
#         """
#         Dynamic Programming
#         Time: O(n)
#         Space: O(n)
#         """
#         n = len(nums)
#         dp = [0] * n
#         dp[0], dp[1] = nums[0], max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-1], dp[i-2]+nums[i])
#         return dp[n-1]


# class Solution4:
#     def rob(self, nums: List[int]) -> int:
#         """
#         Reduce space complexity to O(1)
#         Time: O(n)
#         Space: O(1)
#         """
#         # we know the maximum of money we can rob there
#         # are 1 or 2 houses on the street
#         h0, h1 = nums[0], max(nums[0], nums[1])
#         # then, we start calculate the answer from 3 houses
#         for i in range(2, len(nums)):
#             h0, h1 = h1, max(h0+nums[i], h1)
#         return h1
    

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
res = Solution().rob([1,2,3,1])
print(res)

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
res = Solution().rob([2,7,9,3,1])
print(res)

# max([0, 1, max(1, 0+2)=2, max(2, 1+3)=4, max(4, 2+1)=4]) = 4