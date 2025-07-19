from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Rule: You can not rob the adjacent house.
        Goal: Rob the max amount of money of N houses.
        Initiative: 
            
            max of N house = max(rob house N + max of N-2 house,
                                max of N-1 house)
        """
        # If there is no house, return 0
        if len(nums) == 0:
            return 0
        # Otherwise, decide whether to rob the house or go to next one
        return max((nums[0]+self.rob(nums[2:])), self.rob(nums[1:]))
    

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
ans = Solution().rob(nums=[1,2,3,1])
print(ans)

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
ans = Solution().rob(nums=[2,7,9,3,1])
print(ans)
