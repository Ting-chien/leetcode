from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Intuition: Use DFS/BFS to find max area of island(
        4-direction connected) on the grid.

        Approach:
        1. Travel through all places on grid, if grid[i][j] == 1,
        calculate the max area.
        2. In DFS function, find next step in 4 drectly directions,
        if grid[m][n] == 1, means valid.
        3. Return the max value
        4. (optimize) To prevent repeatly calculate on the same island,
        we should store places we have visited in a global variable

        Complexity:
         - Time: O(M*N), M&N are weidth and length of grid
         - Space: O(M*N), for number of places in grid
        """
        # Global variables
        visited = set()
        max_area = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        M, N = len(grid), len(grid[0])

        # Define a DFS function to find current max area
        def dfs(m, n) -> int:
            """
            Get area of island
            
            :param m: row value
            :param n: col value
            :return: Total value of area
            :rtype: int
            """
            # Add current place to visited
            visited.add((m, n))

            # Set up current place area
            area = 1

            # Look up four directions, and move to next valid place
            for dx, dy in directions:
                nx, ny = m+dx, n+dy
                if (0 <= nx < M) and (0 <= ny < N) \
                    and (grid[nx][ny] == 1) and ((nx, ny) not in visited):
                    area += dfs(nx, ny)

            # Return area
            return area
        
        # Go through all places on grid
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1 and (m, n) not in visited:
                    area = dfs(m, n)
                    max_area = max(max_area, area)

        return max_area
    

# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
res = Solution().maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(res)