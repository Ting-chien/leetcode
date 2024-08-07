class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Divide and conquer
        Time: n log(n)
        Space:
        """
        # return 0 if len(s) < k
        if len(s) < k: return 0

        for c in set(s):
            # split s by c if count of c < k,
            # then find maximum num of length in each subarray
            if s.count(c) < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(c))
        return len(s)
    

# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3
print(Solution().longestSubstring(s="aaabb", k=3))

# Example 2:
# Input: s = "ababbc", k = 2
# Output: 5
print(Solution().longestSubstring(s="ababbc", k=2))
