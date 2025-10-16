from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Intuition: Dynamic Programming ? How ?
        """
        n = len(nums)
        dp = [1] * n  # 每個元素至少能成為長度 1 的序列

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
class Solution:

    def find_leftmost_idx(self, tails: List[int], target: int) -> int:
        left, right = 0, len(tails)-1
        while left <= right:
            middle = (left + right) // 2
            if tails[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            idx = self.find_leftmost_idx(tails, num)
            if idx >= len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)


# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
res = Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18])
print(res)