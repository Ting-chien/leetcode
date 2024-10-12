from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(num: int, path: List[int] = []):
            if len(path) == k or sum(path) >= n:
                if len(path) == k and sum(path) == n:
                    res.append(path)
                return
            for i in range(num, 0, -1):
                backtrack(i-1, path+[i])
        backtrack(9)
        return res
    

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
res = Solution().combinationSum3(k=3, n=7)
print(res)

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
res = Solution().combinationSum3(k=3, n=9)
print(res)