from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        1. Go through number in nums
        2. Add number into curr and compare to target
        3. If curr > target, left ++
        4. If curr < target, right ++
        5. If curr == target, compare with the minimal length
        Time Limit Exceed
        """

        # 方法一：sliding window
        # min_l = float('inf')
        # window = []
        # idx = 0
        # while idx < len(nums):
        #     window.append(nums[idx])
        #     while sum(window) >= target:
        #         min_l = min(min_l, len(window))
        #         window.pop(0)
        #     idx += 1
        # return 0 if isinstance(min_l, float) else min_l

        # 方法二：sliding window
        min_l = float('inf')
        left, right = 0, 0
        curr = 0
        while right < len(nums):
            curr += nums[right]
            while curr >= target:
                min_l = min(min_l, right-left+1)
                curr -= nums[left]
                left += 1
            right += 1
        return 0 if isinstance(min_l, float) else min_l
    

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
print(Solution().minSubArrayLen(target=7, nums=[2,3,1,2,4,3]))

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
print(Solution().minSubArrayLen(target=4, nums=[1,4,4]))

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
print(Solution().minSubArrayLen(target=11, nums=[1,1,1,1,1,1,1,1]))

# Example 4:
# Input: target = 11, nums = [1,2,3,4,5]
# Output: 3
print(Solution().minSubArrayLen(target=11, nums=[1,2,3,4,5]))