from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Intuition: 先知道 nums 的長度並且加總 0+1+2...+n，
        再把總和減去 sum(nums)。

        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        return sum(range(n+1)) - sum(nums)
    

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Intuition: 透過 binary search 找到 idx < num 的
        發生點。
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left