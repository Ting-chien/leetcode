class Solution:
    def compressedString(self, word: str) -> str:
        curr = word[0]
        cnt = 1
        comp = ""
        for i in range(1, len(word)):
            # if the character is equal to the previous one,
            # and cnt < 9, keep accumulate
            if word[i] == word[i-1] and cnt < 9:
                cnt += 1
                continue
            # if not, add cnt and curr character to comp
            comp += f"{cnt}{curr}"
            curr = word[i]
            cnt = 1
        # add the last character
        comp += f"{cnt}{curr}"
        return comp
    

# Example 1:
# Input: word = "abcde"
# Output: "1a1b1c1d1e"
res = Solution().compressedString(word="abcde")
print(res)

# Example 2:
# Input: word = "aaaaaaaaaaaaaabb"
# Output: "9a5a2b"
res = Solution().compressedString(word="aaaaaaaaaaaaaabb")
print(res)