class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Create a 2-dimension DP cache (Since we have base case in 
        # our DP cache, we have to add one more row and column)
        dp = [[float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]

        # Replace value in the base case
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # # Find minimum operations on table
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                # If equal, no extra step
                # if not, find minimum value in insert, delete or replace
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j+1], # insert
                        dp[i+1][j], # delete
                        dp[i+1][j+1] # replace
                    )

        return dp[0][0]

    # def minDistance(self, word1: str, word2: str) -> int:

    #     dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    #     for j in range(len(word2) + 1):
    #         dp[len(word1)][j] = len(word2) - j
    #     for i in range(len(word1) + 1):
    #         dp[i][len(word2)] = len(word1) - i

    #     for i in range(len(word1) - 1, -1, -1):
    #         for j in range(len(word2) - 1, -1, -1):
    #             if word1[i] == word2[j]:
    #                 dp[i][j] = dp[i + 1][j + 1]
    #             else:
    #                 dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
    #     return dp[0][0]
    

# Example 1:
# Input: word1 = "acd", word2 = "abd"
# Output: 1
res = Solution().minDistance("acd", "abd")
print(res)