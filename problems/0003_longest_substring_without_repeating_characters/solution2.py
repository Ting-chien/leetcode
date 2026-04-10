class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window
        Time conplexity: O(n)
        Space complexity:
        """
        window = ""
        max_length = 0
        # iterate the string
        for char in s:
            if char in window:
                # Update left side of window
                window = window.split(char)[1] + char
            else:
                # Update right side of window
                window += char
                max_length = max(max_length, len(window))
        return max_length
    

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
print(Solution().lengthOfLongestSubstring(s="abcabcbb"))

# Example 2:
# Input: s = "bbbbb"
# Output: 1
print(Solution().lengthOfLongestSubstring(s="bbbb"))

# Example 3:
# Input: s = "pwwkew"
# Output: 3
print(Solution().lengthOfLongestSubstring(s="pwwkew"))