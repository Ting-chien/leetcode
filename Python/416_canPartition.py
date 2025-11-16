from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
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