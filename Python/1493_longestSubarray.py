from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        This question is similar to 1004. Max Consecutive Ones III.
        
        Hence, we try to set k = 1, and delete number of 0(which is one)
        when counting consecutive 1.
        """
        fast, slow = 0, 0
        max_cnt = 0 # count of max consecutive 1
        zero_cnt = 0 # count of 0 deleted
        while fast < len(nums):
            # If we met 0, delete it and count 1
            if nums[fast] == 0:
                zero_cnt += 1
            # If we delete 0 more than once
            while zero_cnt > 1:
                if nums[slow] == 0:
                    zero_cnt -= 1
                slow += 1
            # Check max consecutive 1
            max_cnt = max(max_cnt, fast-slow+1-1)
            fast += 1
        return max_cnt
        

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
res = Solution().longestSubarray(nums = [1,1,0,1])
print(res)

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
res = Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1])
print(res)