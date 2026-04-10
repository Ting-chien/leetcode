class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        We need to consider the edge cases of s ot t is empty string
        """
        # Use two pointers to iterate two string
        p1, p2 = 0, 0
        # Start from s first
        while p1 < len(s):
            char = s[p1]
            while p2 < len(t)+1:
                if p2 == len(t):
                    return False
                elif char == t[p2]:
                    p2 += 1
                    break
                else:
                    p2 += 1
            p1 += 1
        return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if s is subsequence of t, return True if valid.

        Condition:
        * Is empty string a subsequence of t ? Yes
        * Can any word be a subsequence of an empty string ? => No

        Intuition: Use a 2 dimension dp to store whether s[:i]
        is a subsquence of t[:j] ?.

        Approach:
        1. Initialize a 2 dimension dp with dp[0][j] = True and
        dp[i][0] = False when i > 0
        2. Iterate through all dp[i][j] with transfer function
        where dp[i][j] = 
            (1) 如果 s[i] == t[j]，那可以選擇用 dp[i-1][j-1] 或 dp[i][j-1]
            來判斷 s 是否為 subsequence
            (2) 如果 s[i] != t[j]，要看 s[:i] 是否為 t[:j-1] 的 subsquence
            ，所以要參考 dp[i][j-1]

            ''    a   c   b
        ''   T.   T   T   T

        a.   F.   T.  T.  T

        b.   F.   F.  F.  T

            ''    a   c   b   f.  c.  b
        ''   T.   T   T   T.  T.  T.  T

        a.   F.   T.  T.  T.  T.  T.  T

        f.   F.   F.  F.  F.  T.  T.  T

        c.   F.   F   F.  F.  F.  T.  T

        b.   F.   F.  F.  F.  F.  T.  T
        """
        m, n = len(s), len(t)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        for j in range(n+1):
            dp[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[m][n]


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# res = Solution().isSubsequence(s = "abc", t = "ahbgdc")
# print(res)
"""
[
      ''    a       h      b    g      f    c
''    [True, True, True, True, True, True, True],
a   [False, True, True, True, True, True, True],
b    [False, False, False, True, True, True, True],
c   [False, False, False, False, False, False, True],
]
"""

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# res = Solution().isSubsequence(s = "axc", t = "ahbgdc")
# print(res)
"""
[
      ''    a.    h.    b.    g.    d.    c
''    [True, True, True, True, True, True, True],
a    [False, True, True, True, True, True, True],
x    [False, False, False, False, False, False, False],
c    [False, False, False, False, False, False, True],
]
"""

# Example 3:
# Input: s = "axc", t = ""
# Output: false
# res = Solution().isSubsequence(s = "axc", t = "")
# print(res)
"""
[[True], [False], [False], [False]]
"""

# Example 4:
# Input: s = "aaaaaa", t = "bbaaa"
# Output: false
res = Solution().isSubsequence(s = "aaaaaa", t = "bbaaa")
print(res)
# [
#       ''    b.     b.    a.    a.    a
# ''    [True, True, True, True, True, True],
# a    [False, False, False, True, True, True],
# a    [False, False, False, True, True, True],
# a    [False, False, False, True, True, True],
# a    [False, False, False, True, True, True],
# a    [False, False, False, True, True, True],
# a    [False, False, False, True, True, True],
# ]
