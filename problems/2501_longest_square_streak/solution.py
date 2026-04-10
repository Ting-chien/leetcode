from typing import List
from math import isqrt


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        m = {}
        nums.sort()
        res = -1
        
        for num in nums:

            # 計算 num 的平方根
            sqrt = isqrt(num)

            # 若 num 是一個完美平方，則計算其開根號的出現次數
            # 並檢查是否為最長的 square streak
            if sqrt*sqrt == num and sqrt in m:
                m[num] = m[sqrt] + 1
                res = max(res, m[num])
            else:
                m[num] = 1

        return res
    

# Example 1:
# Input: nums = [4,3,6,16,8,2]
# Output: 3
res = Solution().longestSquareStreak(nums=[4,3,6,16,8,2])
print(res)

# Example 2:
# Input: nums = [2,3,5,6,7]
# Output: -1
res = Solution().longestSquareStreak(nums=[2,3,5,6,7])
print(res)