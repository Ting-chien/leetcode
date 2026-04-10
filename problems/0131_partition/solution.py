from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(s: List[int], path: List[int] = []):
            # add subset to res
            if s == "":
                res.append(path)
            # iterate through s
            for i in range(len(s)):
                t = s[:i+1]
                if t == t[::-1]:
                    backtrack(s[i+1:], path+[t])
        backtrack(s)
        return res
    

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
res = Solution().partition("aab")
print(res)

# Example 2:
# Input: s = "a"
# Output: [["a"]]
res = Solution().partition("a")
print(res)