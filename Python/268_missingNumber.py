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
    

