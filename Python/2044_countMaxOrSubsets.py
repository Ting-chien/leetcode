from typing import List
from functools import reduce


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_bitwise = float('-inf')
        max_cnt = 0

        def or_bitwise(x: int, y: int):
            return x | y
        
        def dfs(nums: List[int], path: List[int] = []):
            nonlocal max_cnt, max_bitwise
            # if path is not empty, count bitwise OR 
            if path:
                bitwise = reduce(or_bitwise, path)
                if bitwise > max_bitwise:
                    max_bitwise = bitwise
                    max_cnt = 1
                elif bitwise == max_bitwise:
                    max_cnt += 1
            # return if there is no remain integer
            if len(nums) == 0:
                return
            # go through remain integers
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
                
        dfs(nums)
        return max_cnt
    

# Example 1:
# Input: nums = [3,1]
# Output: 2
res = Solution().countMaxOrSubsets(nums=[3,1])
print(res)


# Example 2:
# Input: nums = [2,2,2]
# Output: 7
res = Solution().countMaxOrSubsets(nums=[2,2,2])
print(res)


# Example 3:
# Input: nums = [3,2,1,5]
# Output: 6
res = Solution().countMaxOrSubsets(nums=[3,2,1,5])
print(res)