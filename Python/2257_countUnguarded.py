from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        # 建立一個 m*n 的 grid
        grid = [[0] * n for _ in range(m)]

        # 將 guards 和 walls 標記上位置 (guard=1, wall=2)
        for g in guards:
            row, col = g[0], g[1]
            grid[row][col] = 1
        for w in walls:
            row, col = w[0], w[1]
            grid[row][col] = 2
 
        # 遍歷所有 guards 以及在 guard 的四個方位上標記上 guarded (guarded = 3)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for guard in guards:
            for dir in directions:
                row, col = guard[0]+dir[0], guard[1]+dir[1]
                # 當格子還未走過，且未超出 grid 時
                while 0 <= row < m and 0 <= col < n and grid[row][col] != 2:
                    grid[row][col] = 3
                    row += dir[0]
                    col += dir[1]

        # 遍歷 grid 查看仍然為 0 的數量
        cnt = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    cnt += 1
        return cnt


# Example 1:
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
res = Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])
print(res)

# Example 2:
# Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# Output: 4
res = Solution().countUnguarded( m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])
print(res)