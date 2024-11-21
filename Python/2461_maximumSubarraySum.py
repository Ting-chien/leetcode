from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Time Limit Exceed
        res = 0
        for i in range(0, len(nums)-k+1):
            tmp = nums[i:i+k]
            if len(tmp) == len(set(tmp)):
                res = max(res, sum(tmp))
        return res
    

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # 如果nums的長度小於k，則不可能找到符合條件的subarray
        if len(nums) < k: return 0
        # 初始化第一個 window 裡的總和，以及代表 window 的前後位置的指針
        # 並隨著 window 滑動，減去離開 window 的數字並加上進入 window 的數字
        res, curr = 0, sum(nums[:k])
        i, j = 0, k
        while j <= len(nums):
            print(nums[i:i+k], curr)
            # 檢查 subarray 中的數字是否重複
            if len(set(nums[i:i+k])) == k:
                res = max(res, curr)
            # 將 window 的第一個元素移除，並在最後加入一個新的元素
            if j == len(nums): break
            print(f"res - {nums[i]} + {nums[j]}")
            curr = curr - nums[i] + nums[j]
            i += 1
            j += 1
        return res
    

# # Example 1:
# # Input: nums = [1,5,4,2,9,9,9], k = 3
# # Output: 15
# res = Solution().maximumSubarraySum(nums = [1,5,4,2,9], k = 3)
# print(res)

# # Example 2:
# # Input: nums = [4,4,4], k = 3
# # Output: 0
# res = Solution().maximumSubarraySum(nums = [4,4,4], k = 3)
# print(res)

# Example 3:
# Input: nums = [1,1,1,7,8,9], k = 3
# Output: 24
res = Solution().maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3)
print(res)