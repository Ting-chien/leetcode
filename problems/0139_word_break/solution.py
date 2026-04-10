from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Use a set to increase efficiency
        word_set = set(wordDict)
        # Use a dp table to store if s[0:i] can be segmented
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # If s=""

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
    

