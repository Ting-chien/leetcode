class Solution:
    def climbStairs(self, n: int) -> int:
        """Dynamic Programming (Bottom-up advanced)"""
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a + b
        return b


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