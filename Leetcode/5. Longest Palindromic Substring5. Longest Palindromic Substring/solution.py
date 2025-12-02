class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        透過雙迴圈跑過所有的字串組合，並比對 s[i:j] 和 s[i:j:-1]
        是否一樣。

        Time: O(n^3) - beats 5.01% (really bad 🙃)
        Space: O(1) - beats 59.57%
        """
        max_len = 0
        max_len_str = ""
        n = len(s)
        # 每次取 substring，時間複雜度 O(n^2)
        for i in range(n):
            for j in range(i+1, n+1):
                # 字串反轉 substring[::-1] 時間複雜度 O(n)
                if s[i:j] == s[i:j][::-1] and (j - i) > max_len:
                    max_len = j - i
                    max_len_str = s[i:j]
        return max_len_str
    

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心擴展，透過雙指針往外擴展並比對是否為回文。
        
        Time: O(n^2)
        SPace: O(1)
        """
        n = len(s)

        def expand(l: int, r: int) -> bool:
            """Return longest palindrome from (l,r)"""
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        # Iterate through each start point
        res = ""
        for i in range(n):
            # If odd
            p = expand(i, i)
            if len(p) > len(res):
                res = p
            # If even
            p = expand(i, i+1)
            if len(p) > len(res):
                res = p

        return res
    

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        透過 DP 去計算 s[i:j+1] 是否為 palindrome，轉移
        方程式為 

            dp[i][j] = s[i] == s[j] && ((j-i)<3 || dp[i+1][j-1])

        預設 dp[i][j] 都應該是 False。

        Time: O(n^2)
        Space: O(n^2)
        """
        # Initialize dp
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # For each single character is palindrome
        for i in range(n):
            dp[i][i] = True

        res = ""
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and \
                    ((j - i) < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > len(res):
                        res = s[i:j+1]

        return res
    

# Example 1:
# Input: s = "babad"
# Output: "bab"
print(Solution().longestPalindrome(s = "babad"))

# Example 2:
# Input: s = "a"
# Output: "a"
print(Solution().longestPalindrome(s = "a"))

# Example 2:
# Input: s = "aaaa"
# Output: "aaaa"
print(Solution().longestPalindrome(s = "aaaa"))