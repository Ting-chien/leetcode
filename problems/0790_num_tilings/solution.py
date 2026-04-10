class Solution:
    def numTilings(self, n: int) -> int:
        """
        一刷：2025.8.16（解不出來也看不懂）
        二刷：2025.8.23（還是看不懂解法）
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        elif n == 4:
            return 10
        dp = [0] * (n+1)
        # print(f"dp={dp}")
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        dp[4] = 10
        for i in range(5, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
        return dp[n]
    

# Example 1:
# Input: n = 3
# Output: 5
res = Solution().numTilings(n=3)
print(res)