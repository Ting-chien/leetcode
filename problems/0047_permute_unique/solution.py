from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Use backtrack to record value when possible answer exist
        """
        nums.sort()
        res = []
        N = len(nums)
        def dfs(nums: List[int], path: List[int] = []):
            # return if len(path) == len(nums)
            if len(path) == N:
                res.append(path)
                return
            for i in range(len(nums)):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        dfs(nums)
        return res
    

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
res = Solution().permuteUnique(nums = [1,1,2])
print(res)