class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:

        tmp = [[0] * n for _ in range(n)]

        # Shift in rows
        for i in range(n):
            for j in range(n):
                tmp[i][j] = grid[i][(j+rowShift[i])%n]

        # Shift in cols
        for i in range(n):
            for j in range(n):
                grid[j][i] = tmp[(j+colShift[i])%n][i]

        return grid


class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:

        # Shift in rows
        for i in range(n):
            grid[i] = (grid[i]*2)[rowShift[i]:rowShift[i]+n]

        # Transpose
        for i in range(n):
            for j in range(i, n):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        # Shift in cols
        for j in range(n):
            grid[j] = (grid[j]*2)[colShift[j]:colShift[j]+n]

        # Transpose
        for i in range(n):
            for j in range(i, n):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        return grid


if __name__ == "__main__":

    sol = Solution()

    # Test case 1
    print(sol.cyclicShift(2, [[1,2],[3,4]], [1,0], [0,1])) # [[2, 4], [3, 1]]

    # Test case 2
    print(sol.cyclicShift(3, [[1,2,3],[4,5,6],[7,8,9]], [1,2,0], [2,2,1])) # [[7,8,5],[2,3,9],[6,4,1]]