from typing import List


class Solution:
    MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        n = len(digits)
        res = []
        def backtrack(digits: str, path: str = ""):
            if len(path) == n:
                res.append(path)
                return
            for i in range(len(digits)):
                d = digits[i]
                for j in range(len(self.MAP[int(d)])):
                    char = self.MAP[int(d)][j]
                    backtrack(digits[i+1:], path+char)
        backtrack(digits)
        return res


# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
res = Solution().letterCombinations(digits="23")
print(res)

# Example 2:
# Input: digits = ""
# Output: []
res = Solution().letterCombinations(digits="")
print(res)

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
res = Solution().letterCombinations(digits="2")
print(res)