class Solution:
    def makeFancyString(self, s: str) -> str:

        if len(s) < 3: return s

        res = s[:2]
        for i in range(2, len(s)):
            if s[i] == s[i-1] and s[i-1] == s[i-2]:
                continue
            res += s[i]

        return res
    

# Example 1:
# Input: s = "leeetcode"
# Output: "leetcode"
res = Solution().makeFancyString("leeetcode")
print(res)

# Example 2:
# Input: s = "aaabaaaa"
# Output: "aabaa"
res = Solution().makeFancyString("aaabaaaa")
print(res)