class Solution:
    def removeStars(self, s: str) -> str:
        """
        Use a stack to store characters from s, remove
        the last character once you find a '*' in s.
        """
        stack = []
        for char in s:
            if char == "*":
                stack.pop() if stack else None
            else:
                stack.append(char)
        return "".join(stack)
    

# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"
res = Solution().removeStars(s = "leet**cod*e")
print(res)

# Example 2:
# Input: s = "erase*****"
# Output: ""
res = Solution().removeStars(s = "erase*****")
print(res)