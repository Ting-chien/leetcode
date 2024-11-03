class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): 
            return False
        return goal in s + s


# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true
res = Solution().rotateString(s = "abcde", goal = "cdeab")
print(res)

# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false
res = Solution().rotateString(s = "abcde", goal = "abced")
print(res)

# Example 3:
# Input: s = "defdefdefabcabc", goal = "defdefabcabcdef"
# Output: false
res = Solution().rotateString(s = "defdefdefabcabc", goal = "defdefabcabcdef")
print(res)
