import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        This problem is not a math problem that can be solved in one equation.
        Instead, it envolved algorithm to find the minimum value of eating
        speed k.

        To find k, binary search is a good way to try and test. For example, 
        if piles = [3,6,7,11] and h = 8, the max k is 11 and min k is 1. So,
        we can start from the middle (11+1)/2 = 6.

            k=6, 
                3 / 6 = 0 ... 3 => 1hr
                6 / 6 = 1 ... 0 => 1hr
                7 / 6 = 1 ... 1 => 2hr
                11 / 6 = 1 ... 5 => 2hr
                -------------------------
                Total: 6hr < 8hr (k can be smaller)

            k=(1+6)//2=3
                3 / 3 = 1 ... 0 => 1hr
                6 / 3 = 2 ... 0 => 2hr
                7 / 3 = 2 ... 1 => 3hr
                11 / 3 = 3 ... 2 => 4hr
                -------------------------
                Total: 10hr > 8hr (k should be bigger)

            k=(3+6)//2=4
                3 / 4 = 0 ... 3 => 1hr
                6 / 4 = 1 ... 2 => 2hr
                7 / 4 = 1 ... 3 => 2hr
                11 / 4 = 2 ... 3 => 3hr
                -------------------------
                Total: 8hr = 8hr Great! 🥳
        """

        left, right = 1, max(piles)

        def can_finish(piles: List[int], k: int, h: int) -> bool:
            """
            Check whether Koko can finish all bananas in k speed.
            """
            cnt = 0
            for p in piles:
                cnt += math.ceil(p / k)
            return cnt <= h
        
        while left < right:
            mid = (left + right) // 2
            if can_finish(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return right
    

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8))