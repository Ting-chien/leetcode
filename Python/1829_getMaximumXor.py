from typing import List
from functools import reduce


class Solution1:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        # Iterate numbers in nums from high to low index
        # e.g. [0,1,2,3] -> [0,1,2] -> [0,1] -> [0]
        for i in range(len(nums), 0, -1):
            max_xor = 0
            max_k = 0
            # Iterate through all possible k, which 0 <= k < 2^maxBit
            for k in range(2**maximumBit):
                curr = reduce(lambda x, y: x ^ y, nums[:i] + [k])
                if curr > max_xor:
                    max_xor = curr
                    max_k = k
            ans.append(max_k)
        return ans
    

class Solution2:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        all_xor = reduce(lambda x, y: x ^ y, nums)
        max_xor = (2 ** maximumBit) - 1
        # 從nums尾部開始逐一移除數字，並透過XOR計算取得k
        res = []
        for i in range(len(nums)-1, -1, -1):
            res.append(all_xor ^ max_xor)
            all_xor ^= nums[i]
        return res
    

# Example 1:
# Input: nums = [0,1,1,3], maximumBit = 2
# Output: [0,3,2,3]
res = Solution2().getMaximumXor(nums = [0,1,1,3], maximumBit = 2)
print(res)

# Example 2:
# Input: nums = [2,3,4,7], maximumBit = 3
# Output: [5,2,6,5]
res = Solution2().getMaximumXor(nums = [2,3,4,7], maximumBit = 3)
print(res)

# Example 3:
# Input: nums = [0,1,2,2,5,7], maximumBit = 3
# Output: [4,3,6,4,6,7]
res = Solution2().getMaximumXor(nums = [0,1,2,2,5,7], maximumBit = 3)
print(res)