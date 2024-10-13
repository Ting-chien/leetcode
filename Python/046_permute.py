from typing import List, Set


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """此題透過 backtrack 的概念，來將 nums 裡的數字逐一
        走過，並在每一層扣掉上一層使用過的數字，當最後蕾幾的數量
        與最初 nums 一樣時則代表走完。
        """
        res = []
        def backtrack(remains: List[int], path: List[int]):
            nonlocal res
            # set condition for return
            if len(path) == len(nums):
                res.append(path[:])
                return
            # general case
            for i in range(len(remains)):
                num = remains[i]
                path.append(num)
                backtrack(remains[:i]+remains[i+1:], path)
                path.pop()
        backtrack(nums, [])
        return res
    

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(nums: Set[int], path: List[int] = []):
            """
            :param nums: Current numbers can be chosen.
            :param nums: Permutation result
            """
            # return if length of path is n
            if len(path) == n:
                res.append(path)
                return
            # go through remain num in nums
            for num in nums:
                backtrack(nums-{num}, path+[num])
        backtrack(set(nums))
        return res
    

# Example 1
nums = [1,2,3]
print(Solution2().permute(nums))

# Example 2
nums = [0, 1]
print(Solution2().permute(nums))

# Example 3
nums = [1]
print(Solution2().permute(nums))