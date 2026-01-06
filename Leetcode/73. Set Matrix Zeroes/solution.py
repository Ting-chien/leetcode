from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # Find all rows and cols where exist zero
        zero_rows = set()
        zero_cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Update matrix in-place where row in zero_rows, and
        # column in zero_cols
        for r in zero_rows:
            for c in range(n):
                matrix[r][c] = 0
        for r in range(m):
            for c in zero_cols:
                matrix[r][c] = 0

        print(matrix)

# Example 1
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
Solution().setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])