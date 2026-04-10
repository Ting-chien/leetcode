class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        def dfs(row: int, col: int):
            if row == m-1 and col == n-1:
                nonlocal count
                count += 1
            if 0 <= row < m and 0 <= col < n:
                dfs(row+1, col) # Go right
                dfs(row, col+1) # Go down
        dfs(0, 0)
        return count
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Optimize: Memorization

            Time: O(m*n)
            Space: O(m*n)
        """
        memo = {} # Use (row,col) as a key in memo
        def dfs(col: int, row: int):
            # Find a valid path
            if col == m-1 or row == n-1:
                return 1
            # Find an existing answer
            if (row, col) in memo:
                return memo[(row, col)]
            paths = dfs(col+1, row) + dfs(col, row+1)
            memo[(row, col)] = paths
            return paths
        return dfs(0, 0)
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        2-dimension dynamic program
        
            Time: O(m*n)
            Space: O(m*n)
        """
        matrix = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[m-1][n-1]
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        2-dimension dynamic program
        
        Complexity
        * Time: O(m*n)
        * Space: O(m*n)
        """
        dp = [[0] * n for _ in range(m)]
        # 第一列和第一行的路徑數都是1（只能往右或往下）
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
    

if __name__ == '__main__':

    sol = Solution()

    # Test case 1
    print(sol.uniquePaths(m=3, n=2))

    # Test case 2
    print(sol.uniquePaths(m=3, n=7))