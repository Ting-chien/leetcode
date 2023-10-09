class Solution:
    def climbStairs(self, n: int) -> int:
        """Dynamic Programming (Bottom-up)"""
        res = [None]*(n+1)
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1]


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