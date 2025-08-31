from typing import List


class Solution:

    def kadane(self, nums: List[int]):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        In 53. Maximum Subarray, we know how to find maximum
        subarry by Kadane's Algorithm. Now, we have to explore
        the array into circular circumstance.

        在這種情況，我們可以假設答案有兩種
        1. Maximum subaraay 在陣列中間，算法就跟 Leetcode 53 一樣
        2. Maximum subaraay 由頭尾組成，這時候就變成油 sum(nums) - minimum array
        """
        max_sum = self.kadane(nums)
        min_sum = self.kadane([n*(-1) for n in nums]) * (-1)
        total = sum(nums)
        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, total-min_sum)
