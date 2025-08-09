from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Use a DFS function to find all connected cities and update
        grid[m][m] to 0, and traverse all grid when grid[m][n] is 1.

        Approach
        1. Every time find grid[m][m] == 1, cnt += 1
        2. Start from grid[m][m] == 1 to find all connected cities by DFS
        3. In DFS, we look up four direction where is inside the grid and
        grid[m][n] == 1, move to the next field if valid

        ❌ 錯誤方向，這題的 isConnected 是代表城市和城市之間的關係，而不是一張網格，
        因此要用一唯的方向去做。
        """
        cnt = 0
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        # A DFS to traverse all connected cities
        def dfs(row: int, col: int):
            # Set city = 0 as visited
            isConnected[row][col] = 0
            # Walk through four direction
            for d in directions:
                next_row = row + d[0]
                next_col = col + d[1]
                if 0 <= next_row < n and 0 <= next_col < n and isConnected[next_row][next_col] == 1:
                    dfs(next_row, next_col)

        # Look up the grid
        n = len(isConnected)
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    cnt += 1
                    dfs(row, col)
        
        return cnt
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Use a list to stoare visited cities, if a city is visited,
        set visited[city] = True. For loop each city, and use DFS
        to find all connected cities.

        🌟 記得！在找這種關聯關係時，DFS 可以一路往下找到所有關聯，特別好用👍🏻
        """

        n = len(isConnected)
        visited = [False] * n

        def dfs(city: int):
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and not visited[next_city]:
                    visited[next_city] = True
                    dfs(next_city)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                provinces += 1
                visited[city] = True
                dfs(city)

        return provinces
    

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
res = Solution().findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]])
print(res)

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
res = Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
print(res)

# Example 3:
# Input: isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# Output: 1
res = Solution().findCircleNum(isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
print(res)

[
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]