from typing import List
from functools import reduce, cache


class Solution1:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        Time Limit Exceed
        """
        max_len = 0
        def dfs(nums: List[int], path: List[int] = []):
            # 計算當下排列組合的 AND bitwise value
            # 若 bitwise > 0，則
            if path:
                nonlocal max_len
                val = reduce(lambda x, y: x & y, path)
                if val > 0: 
                    max_len = max(max_len, len(path))
            # 往下遍歷所有數字直到 nums 為空
            if len(nums) == 0:
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
        dfs(candidates)
        return max_len
    
class Solution2:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        """
        max_len = 0
        N = len(candidates)

        @cache
        def dfs(s: int, curr: int, cnt: int):
            # 計算當下排列組合的 AND bitwise value
            # 若 bitwise > 0，則
            nonlocal max_len
            if curr > 0:
                max_len = max(max_len, cnt)
            # 往下遍歷所有數字直到 s==N
            if s == N:
                return
            for i in range(s, N):
                dfs(i+1, curr&candidates[i], cnt+1)
        
        dfs(0, candidates[0], 0)
        return max_len
    
class Solution3:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        https://algo.monster/liteproblems/2275
        """
        max_cnt = 0
        # 遍歷 0~31 位元，並針對 candidates 中所有的數字去計算第 i 位元
        # 上是 1 的數字並加總，加總的和及代表排列組合中的數量
        for i in range(32):
            cnt = 0
            for num in candidates:
                if (num >> i) & 1:
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt
    

# Example 1:
# Input: candidates = [16,17,71,62,12,24,14]
# Output: 4
# res = Solution2().largestCombination([16,17,71,62,12,24,14])
# print(res)

# Example 2:
# Input: candidates = [8,8]
# Output: 2
# res = Solution2().largestCombination([8,8])
# print(res)

# Example 3:
# Input: candidates = [84,40,66,44,91,90,1,14,73,51,47,35,18,46,18,65,55,18,16,45,43,58,90,92,91,43,44,76,85,72,24,89,60,94,81,90,86,79,84,41,41,28,44]
# Output: 28
res = Solution3().largestCombination([84,40,66,44,91,90,1,14,73,51,47,35,18,46,18,65,55,18,16,45,43,58,90,92,91,43,44,76,85,72,24,89,60,94,81,90,86,79,84,41,41,28,44])
print(res)