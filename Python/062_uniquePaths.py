class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """2-dimension dynamic program"""
        matrix = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[m-1][n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        def dp(col: int, row: int):
            nonlocal m, n
            if col == m-1 or row == n-1:
                return 1
            return dp(col+1, row) + dp(col, row+1)
        return dp(0, 0)

    

if __name__ == '__main__':

    sol = Solution()

    # Test case 1
    print(sol.uniquePaths(m=3, n=2))

    # Test case 2
    print(sol.uniquePaths(m=3, n=7))