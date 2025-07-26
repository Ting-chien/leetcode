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
    

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
res = Solution().isSubsequence(s = "abc", t = "ahbgdc")
print(res)

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
res = Solution().isSubsequence(s = "axc", t = "ahbgdc")
print(res)

# Example 3:
# Input: s = "axc", t = ""
# Output: false
res = Solution().isSubsequence(s = "axc", t = "")
print(res)

# Example 4:
# Input: s = "aaaaaa", t = "bbaaa"
# Output: false
res = Solution().isSubsequence(s = "aaaaaa", t = "bbaaa")
print(res)