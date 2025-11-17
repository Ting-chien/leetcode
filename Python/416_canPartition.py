from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Time Limit Exceed
        
        Time: O(2^n) 選 或 不選
        Space: O(n) Decision tree 最高為 n
        """
        
        # Check if subnet is valid
        if sum(nums) % 2 != 0:
            return False
        
        # Find length of nums and target
        n = len(nums)
        target = sum(nums) / 2

        # Find subnet that sum is equal to target
        is_equal = False
        memo = {}
        def dfs(start: int, curr: int):

            nonlocal is_equal
            if curr == target:
                is_equal = True
                return
            
            if start >= n:
                return
            
            for i in range(start, n):
                if curr + nums[i] <= target:
                    dfs(i+1, curr+nums[i])

        dfs(0, 0)
        return is_equal
    

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Memorization
        
        Time: O(n*target)
        Space: 
        """

        # 檢查 subnets 是否有機會存在
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        # 每個 subnet 要加總的目標
        n = len(nums)
        target = total // 2

        # 建立 memo 來提前剪枝
        memo = {}

        def dfs(i, curr) -> bool:
            # Edge case
            if curr == 0:
                return True
            if i < 0 or curr < 0:
                return False
            # General case
            if (i, curr) not in memo:
                memo[(i, curr)] = dfs(i-1, curr-nums[i]) or dfs(i-1, curr)
            return memo[(i, curr)]
        
        return dfs(n-1, target)
    

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """2D Dynamic Programming"""

        # 檢查 subnets 是否有機會存在
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        # 每個 subnet 要加總的目標
        n = len(nums)
        target = total // 2

        # 建立一個長寬為 (n+1)*(target+1) 的 dp
        dp = [[False] * (target+1) for _ in range(n+1)]

        # 將 target == 0 的情況設為 True
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1] > j:
                    # 不能選
                    dp[i][j] = dp[i-1][j]
                else:
                    # 選和不選
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]

        return dp[n][target]


# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
print(Solution().canPartition(nums = [1,5,11,5]))

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
print(Solution().canPartition(nums = [1,2,3,5]))

# Example 3:
# Input: nums = [1,2,5]
# Output: false
print(Solution().canPartition(nums = [1,2,5]))