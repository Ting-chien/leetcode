from typing import List


class Solution:

    def dfs(self, fish: int, m: int, n: int, M: int, N: int, grid: List[List[int]]):
        """
        Find next water cell and catch fish, return if no water exist.

        Args:
            fish: Current fish caught by fisher
            m: Current x cooridinate
            n: Current y cooridinate            
            M: Boundary of x direction
            N: Boundary of y direction
            grid: M*N cells
        """
        # turn number of fish to 0 if they have been cuaght
        grid[m][n] = 0
        # find another water cell and catch fish
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in directions:
            next_x = m + d[0]
            next_y = n + d[1]
            if 0 <= next_x < M and 0 <= next_y < N and grid[next_x][next_y] > 0:
                fish += self.dfs(
                    fish=grid[next_x][next_y],
                    m=next_x,
                    n=next_y,
                    M=M,
                    N=N,
                    grid=grid
                )
        return fish

    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        Intuition:
        1. Go through all cells in grid.
        2. Find maximum fish can get by DFS starting from a water cell.
        """
        max_fish = 0 # maximum number of fish can catch

        # go through each cell in grid and catch fish start from water cell
        M, N = len(grid), len(grid[0])
        for m in range(M):
            for n in range(N):
                if grid[m][n] > 0:
                    max_fish = max(max_fish, self.dfs(
                        fish=grid[m][n],
                        m=m,
                        n=n,
                        M=M,
                        N=N,
                        grid=grid
                    ))

        return max_fish
    

# Example 1:
# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
res = Solution().findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]])
print(res)

# Example 2:
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
# Output: 1
res = Solution().findMaxFish(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
print(res)

# Example 3:
# Input: grid = [[10,5],[8,0]]
# Output: 23
res = Solution().findMaxFish(grid = [[10,5],[8,0]])
print(res)