class Solution:
    def climbStairs(self, n: int) -> int:
        """recursive (Time Limit Exceeded in n=44)"""
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    

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