from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:

        M, N = len(mat), len(mat[0])
        areas = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Use dfs to find all possible area
        area = 0
        def dfs(m: int, n: int):

            # Update current area and cell
            nonlocal area
            area += 1
            mat[m][n] = 0

            # Travel four direction
            for dx, dy in directions:
                next_x, next_y = m + dx, n + dy
                print(f"next_x={next_x}, next_y={next_y}")
                if 0 <= next_x < M and 0 <= next_y < N and mat[next_x][next_y] == 1:
                    dfs(next_x, next_y)

        for m in range(M):
            for n in range(N):
                if mat[m][n] == 1:
                    dfs(m, n)
                    areas.append(area)
                    area = 0 
        print(f"All possible areas: {areas}")

        # Check if those areas are square get get two of them with same side legth


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.maxArea(mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]])) # Output: 4

    # Test cases 2
    print(solution.maxArea(mat = [[0,1],[1,0]])) # Output: 1

    # Test cases 3
    print(solution.maxArea(mat = [[0,0],[0,1]])) # Output: 0