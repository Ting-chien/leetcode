from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sort first
        nums.sort()
        # Two pointers start from left and right side of array
        l, r = 0, len(nums)-1
        cnt = 0
        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                l += 1
                r -= 1
                cnt += 1
        return cnt


# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
res = Solution().maxOperations(nums = [1,2,3,4], k = 5)
print(res)

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
res = Solution().maxOperations(nums = [3,1,3,4,3], k = 6)
print(res)