class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Use top-down DP

            n=5
            i=5, dp[5]=7, find dp[4], dp[3], dp[2]
            i=4, dp[4]=4, find dp[3], dp[2], dp[1]
            i=3, dp[3]=2, find dp[2], dp[1], dp[0]
            i=2, dp[2]=1
            i=1, dp[1]=1
            i=0, dp[0]=0

        Complexity
        * Time: O(n) - beats 100%
        * Space: O(n) - beats 47.88%
        """
        dp = [None] * (n+1)
        def dfs(i: int):
            if i == 0 or i == 1 or i == 2:
                return 0 if i == 0 else 1
            if not dp[i]:
                dp[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return dp[i]
        return dfs(5)


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Use bottom-up DP

        Complexity
        * Time: O(n) - beats 100%
        * Space: O(n) - beats 78.18%
        """
        if n == 0 or n == 1 or n == 2:
            return 0 if n == 0 else 1
        dp = [None] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Use bottom-up DP

        Complexity
        * Time: O(n) - beats 100%
        * Space: O(1) - beats 7.68%
        """
        if n == 0 or n == 1 or n == 2:
            return 0 if n == 0 else 1
        a, b, c = 1, 1, 0
        for _ in range(3, n+1):
            a, b, c = a+b+c, a, b
        return a
