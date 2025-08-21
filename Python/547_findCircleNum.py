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
    

class Solution:

    parents = []
    count = 0

    def find(self, x: int) -> int:
        """
        用來找到 x 的跟節點並作路徑壓縮，這個步驟很重要，有可能
        原本的路徑關係是

            a -> b -> c -> ... -> h

        透過地回的方式往下找才能找到真正的 root 並幫助下一次搜尋
        只需要花費 O(1) 的時間。
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x: int, y: int):
        """
        透過 union by rank/size，把小的樹掛到大的樹做 flatten
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parents[root_y] = root_x
            self.count -= 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        嘗試用 Union Find 的方式去找出所有 connected 的 cities。
        """
        n = len(isConnected)
        self.count = n
        self.parents = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.union(i, j)

        return self.count
    

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