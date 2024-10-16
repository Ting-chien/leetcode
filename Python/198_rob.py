from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
        """
        RecursionError: maximum recursion depth exceeded in comparison
        """
        def dfs(n):
            """
            :param n: Number of house remain to be robbed
            """
            # if no house to rob
            if n == 0:
                return 0
            # else, compare robbing n-1th or n-2th house
            return max(dfs(n-1), dfs(n-2)+nums[n])
        return dfs(len(nums)-1)
    

class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        Use cache to prevent calculate repetely
        Time: O(n)
        Space: O(n)
        """
        cache = [-1] * len(nums)
        def dfs(n):
            """
            :param n: Number of house remain to be robbed
            """
            # if no house to rob
            if n < 0:
                return 0
            # else, compare robbing n-1th or n-2th house
            if cache[n] != -1:
                return cache[n]
            res = max(dfs(n-1), dfs(n-2)+nums[n])
            return res
        return dfs(len(nums)-1)
    

class Solution3:
    def rob(self, nums: List[int]) -> int:
        """
        Dynamic Programming
        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]


class Solution4:
    def rob(self, nums: List[int]) -> int:
        """
        Reduce space complexity to O(1)
        Time: O(n)
        Space: O(1)
        """
        # we know the maximum of money we can rob there
        # are 1 or 2 houses on the street
        h0, h1 = nums[0], max(nums[0], nums[1])
        # then, we start calculate the answer from 3 houses
        for i in range(2, len(nums)):
            h0, h1 = h1, max(h0+nums[i], h1)
        return h1
    

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
res = Solution3().rob([1,2,3,1])
print(res)

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
res = Solution3().rob([2,7,9,3,1])
print(res)