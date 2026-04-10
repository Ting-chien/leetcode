class Solution1:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Alogrithm:
        1. Find all substring with length equal 3
        """
        N = len(s)
        res = set() # Use set to store substring to prevent duplicate answer
        def dfs(start: int, curr: str):
            """
            Args:
                start: Current index to go through string s
                curr: Current substring
            """
            if len(curr) == 3:
                # Check if substring is palindrome
                if curr[0] == curr[-1]:
                    res.add(curr)
                return
            if start == N:
                return
            for i in range(start, N):
                dfs(i+1, curr+s[i])
        dfs(0,"")
        return len(res)
    

class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        res = 0
        for letter in letters:
            # 找到 s 中第一個和最後一個 letter 的位置
            l, r = s.index(letter), s.rindex(letter)
            # 將 l, r 之間所有不同字元的數量記錄下來（不同字元即代表不同的回文種類）
            between = set()
            for i in range(l+1, r):
                between.add(s[i])
            res += len(between)
        return res
    

# Example 1:
# Input: s = "aabca"
# Output: 3
res = Solution2().countPalindromicSubsequence(s = "aabca")
print(res)

# Example 2:
# Input: s = "adc"
# Output: 0
res = Solution2().countPalindromicSubsequence(s = "adc")
print(res)

# Example 3:
# Input: s = "bbcbaba"
# Output: 4
res = Solution2().countPalindromicSubsequence(s = "bbcbaba")
print(res)