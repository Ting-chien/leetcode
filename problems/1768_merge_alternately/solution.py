class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Concatenate word1 and word2 alternatively, and append
        the remain string to the end.

        Edge cases:
        1. Would word1 or word2 an empty string ? => No
        """
        # Get base length of concatenate string
        base_len = min(len(word1), len(word2))
        # Iterate through word1 and word2
        i = 0
        res = ""
        while i < base_len:
            res += word1[i]
            res += word2[i]
            i += 1
        # Append remain string
        res += word1[i:]
        res += word2[i:]
        return res
    

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
res = Solution().mergeAlternately(word1 = "abc", word2 = "pqr")
print(res)

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
res = Solution().mergeAlternately(word1 = "ab", word2 = "pqrs")
print(res)
