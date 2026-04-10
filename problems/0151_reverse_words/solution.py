class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Intuition
        1. Turn words into list
        2. Reverse list

        PS. Reverse function in Python take O(n) and O(1) in
        time and space complexity.
        """
        s = s.strip() # Remove leading and trailing space
        l = s.split() # Split words by space
        l.reverse() # Reverse the list
        return " ".join(l)
    

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
res = Solution().reverseWords("the sky is blue")
print(res)

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
res = Solution().reverseWords("  hello world  ")
print(res)

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
res = Solution().reverseWords("a good   example")
print(res)