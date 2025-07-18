from typing import List, Set


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        letters = {"a", "b", "c"}
        def dfs(option: Set[str], curr: str):
            if len(curr) == n:
                res.append(curr)
                return
            for char in option:
                nonlocal letters
                letters.remove(char)
                dfs(letters, curr+char)
                letters = {"a", "b", "c"}
        dfs(option=letters, curr="")
        return res


# Example 3:
# Input: n = 3, k = 9
# Output: "cab"
res = Solution().getHappyString(3, 9)
print(res) # "cab"