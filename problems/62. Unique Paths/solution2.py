class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """recursive (Time Limit Exceeded)"""
        return self.find_path(m, n, 0, 0)
    def find_path(self, m, n, col, row):
        if col == m-1 or row == n-1:
            return 1
        return self.find_path(m, n, col+1, row) + self.find_path(m, n, col, row+1)
    

if __name__ == '__main__':

    sol = Solution()

    # Test case 1
    print(sol.uniquePaths(m=3, n=2))

    # Test case 2
    print(sol.uniquePaths(m=3, n=7))