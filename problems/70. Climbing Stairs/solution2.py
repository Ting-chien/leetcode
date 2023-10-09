from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        """Dynamic Programming (Top-down)"""
        def dp(n: int, res: List[int]):
            if n == 1 or n == 2:
                return n
            if not res[n]:
                res[n] = dp(n-1, res) + dp(n-2, res)
            return res[n]
        return dp(n, [None]*(n+1))
    

if __name__ == '__main__':

    sol = Solution()

    # Test case 1
    n = 2
    print(sol.climbStairs(n=2))

    # Test case 2
    n = 5
    print(sol.climbStairs(n=5))

    # Test case 3
    n = 44
    print(sol.climbStairs(n=44))
