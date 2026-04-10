from typing import List


class Solution2:
    '''BFS
        Time: O(n^2)
        Space: O(n^2)
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        num = len(grid) # length of the grid
        nextSteps = [[0, 0]] # array used to record next direction
        distance = 1
        steps = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ] # eight directions can move

        grid[0][0] = 1
        while nextSteps:
            for _ in range(len(nextSteps)):
                row, col = nextSteps.pop(0)
                # return conditin
                # 因為 BFS 特性，可以在這裡提早返回，因為已找到最短距離
                if row == num-1 and col == num-1: return distance
                for step in steps:
                    next_row = row + step[0]
                    next_col = col + step[1]
                    # Skip this step if out of the grid
                    if next_row >= 0 and next_col >= 0 and next_row < num and next_col < num and grid[next_row][next_col] == 0:
                        grid[next_row][next_col] = 1
                        nextSteps.append([next_row, next_col])
            distance += 1
        
        return -1


class Solution3:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        DFS
            Time: O(2^{n^2})
            Space: O(n^2)
        """

        # 如果起點為(1,1)，則代表無可行道路
        if grid[0][0] == 1: return -1

        M, N = len(grid), len(grid[0])
        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        min_cnt = float('inf')

        def dfs(m, n, cnt):
            if m == M-1 and n == N-1:
                nonlocal min_cnt
                min_cnt = min(cnt, min_cnt)
                return
            for d in directions:
                x, y = d[0], d[1]
                if 0 <= m+x < M and 0 <= n+y < N and grid[m+x][n+y] == 0:
                    grid[m][n] = 1 # 將走過的路標為1
                    dfs(m+x, n+y, cnt+1)
                    grid[m][n] = 0 # 走完後再標回0
        grid[0][0] = 1
        dfs(0, 0, 1)
        return min_cnt if min_cnt != float('inf') else -1

        

if __name__ == '__main__':
    # print(Solution3().shortestPathBinaryMatrix([[0,1],[1,0]])) # 2
    print(Solution3().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])) # 4
    # print(Solution3().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])) # -1