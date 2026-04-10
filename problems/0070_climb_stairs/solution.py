class Solution1:
    '''Recursion'''
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution2:
    '''DP(Top-down)'''
    def climbStairs(self, n: int) -> int:
        return self.dp(n, [None]*(n+1))

    def dp(self, n, result):
        if n == 1 or n == 2:
            return n
        if not result[n]:
            result[n] = self.dp(n-1, result) + self.dp(n-2, result)
        return result[n]

class Solution3:
    '''DP(bottom up)'''
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
class Solution4:
    '''DP(Bottom-up)'''
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n
        a, b = 1, 2
        for i in range(3, n):
            a, b = b, a+b
        return a + b

if __name__ == '__main__':
    sol = Solution3()
    print(sol.climbStairs(4))