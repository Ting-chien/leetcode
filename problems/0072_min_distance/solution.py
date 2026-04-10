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
    

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        We got two string word1, word2, trying to tansfer word1
        to word2 by insert, delete or replace.

        Get minimum of operation we need to transfer word1 to 
        word2.

        Condition:
        * 0 <= word1.length, word2.length <= 500

        Intuition:

            word1: a    b    c
            word2: a    d    c

            if i=0, j=0 => match => do nothing
            if i=1, j=1 => mismatch => find min in three operation
            * insert, 
            * delete,
            * replace

        Approach:
        1. Initialize a 2 dimension DP table
        2. Starting from empty string
        3. Counting from 1~n+1 with algorithm above

        Complexity:
        * Time O(n*m) n: length of word1, m: length of word2
        * Space O(n*m)
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i or j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[m][n]
        

    

# Example 1:
# Input: word1 = "acd", word2 = "abd"
# Output: 1
res = Solution().minDistance("acd", "abd")
print(res)

# Example 2:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
res = Solution().minDistance(word1 = "horse", word2 = "ros")
print(res)