from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Move the window with the width=k, and calculate average
        value of elements in window

        Edge cases question:
        1. Is len(nums) and k be 0 ? No

        First submit: Time Limit Exceed
        """
        # # Check if nums larger or equal to k
        # if len(nums) < k:
        #     pass
        #     # Not gonna happend, since k <= n

        max_val = float("-inf")
        for i in range(len(nums)-k+1):
            avg = sum(nums[i:i+k]) / k # 不用每次都算平均，其實只要算總合就好
            max_val = max(max_val, avg)
        return max_val
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Move the window with the width=k, and calculate average
        value of elements in window

        Edge cases question:
        1. Is len(nums) and k be 0 ? No

        First submit: Time Limit Exceed
        """
        max_val = float("-inf")
        for i in range(len(nums)-k+1):
            max_val = max(max_val, sum(nums[i:i+k]))
        return max_val / k
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        不用每次算總和，只要加上新的數字和移除舊的數字
        """
        max_val = curr = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            # print("Before")
            # print(f"max_val={max_val}, curr={curr}")
            curr = curr - nums[i-1] + nums[i+k-1]
            max_val = max(max_val, curr)
            # print("After")
            # print(f"max_val={max_val}, curr={curr}")
        return max_val / k
    

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
res = Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
print(res)

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000
res = Solution().findMaxAverage(nums = [5], k = 1)
print(res)

# Example 3:
# Input: nums = [3,3,4,3,0], k = 3
# Output: 5.00000
res = Solution().findMaxAverage(nums = [3,3,4,3,0], k = 3)
print(res)