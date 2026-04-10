from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        
        # Sort nums
        nums.sort()

        # Iterate through nums and find max consecutive length
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            elif nums[i] - nums[i-1] == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1

        return max(res, cnt)
    

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
res = Solution().longestConsecutive(nums = [100,4,200,1,3,2])
print(res)

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
res = Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
print(res)

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3
res = Solution().longestConsecutive(nums = [1,0,1,2])
print(res)