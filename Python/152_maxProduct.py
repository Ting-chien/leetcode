import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        約 40 分鐘寫出正確解
        """
        
        # n = len(nums)
        # dp = [float('-inf')] * n

        # Submission 1: Wrong answer
        # for i in range(1, n):
        #     dp[i] = max(dp[i-1]*nums[i], nums[i])

        # Submission 2: TLE
        # for i in range(n):
        #     for j in range(i+1):
        #         dp[i] = max(math.prod(nums[j:i+1]), dp[i])

        n = len(nums)
        dp = [[float('inf'), float('-inf')] for _ in range(n)] # (最小值, 最大值)
        dp[0] = [nums[0], nums[0]]

        for i in range(1, n):
            num = nums[i]
            dp[i] = [
                min(dp[i-1][0]*num, dp[i-1][1]*num, num),
                max(dp[i-1][0]*num, dp[i-1][1]*num, num)
            ]

        return max([_dp[1] for _dp in dp])
    

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        看答案寫出最佳解
        """

        curr_max = nums[0]
        curr_min = nums[0]
        res = curr_max

        for i in range(1, len(nums)):
            num = nums[i]
            tmp_max = curr_max
            curr_max = max(tmp_max*num, curr_min*num, num)
            curr_min = min(tmp_max*num, curr_min*num, num)
            # print(f"curr_max={curr_max}, curr_min={curr_min}")
            res = max(res, curr_max)
            # print(f"res={res}")

        return res
    

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
res = Solution().maxProduct(nums = [2,3,-2,4])
print(res)

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
res = Solution().maxProduct(nums = [-2,0,-1])
print(res)

# Example 3:
# Input: nums = [-2,3,-4]
# Output: 24
res = Solution().maxProduct(nums = [-2,3,-4])
print(res)

# Example 4:
# Input: nums = [0, 2]
# Output: 2
res = Solution().maxProduct(nums = [0, 2])
print(res)