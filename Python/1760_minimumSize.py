from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # You can do the operation at most maxOperations times
        for _ in range(maxOperations):
            # Each time find the maximum number in nums, and divided by 2
            max_num = max(nums)
            nums.remove(max_num)
            a, b = max_num // 2, max_num - (max_num // 2)
            print(a, b)
            nums += [a, b]
        return nums
    

# Example 1:
# Input: nums = [9], maxOperations = 2
# Output: 3
res = Solution().minimumSize(nums = [9], maxOperations = 2)
print(res)
