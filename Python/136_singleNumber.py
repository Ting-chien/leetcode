from typing import List
from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Complexity
        * Time: O(n) - beats 100%
        * Space: O(1) - beats 21.08%
        """
        res = 0
        for num in nums:
            res ^= num
        return res
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return reduce(xor, nums)
        return reduce(lambda x, y: x ^ y, nums)