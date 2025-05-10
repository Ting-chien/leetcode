from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Boundary
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        # Vars need to be used
        num = len(grid) # length of the grid
        nextSteps = [[0, 0, 1]] # array used to record next direction and distance
        visited = {"[0, 0]": 1} # recording which square already been go through
        steps = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ] # eight directions can move

        while nextSteps:
            print(nextSteps)
            row, col, distance = nextSteps.pop(0)
            # return conditin
            if row == num-1 and col == num-1: return distance
            for step in steps:
                next_row = row + step[0]
                next_col = col + step[1]
                # Skip this step if out of the grid
                if not (next_row >= 0 and next_col >= 0 and next_row < num and next_col < num and grid[next_row][next_col] == 0): continue
                # Add next step into nextSteps array
                if f'[{next_row}, {next_col}]' not in visited:
                    visited[f'[{next_row}, {next_col}]'] = 1
                    nextSteps.append([next_row, next_col, distance+1])
        
        return -1

class Solution2:
    '''Try to improve memory usage by turning grid situation directly'''
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
        M, N = len(grid), len(grid[0])
        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        min_cnt = float('inf')

        def dfs(m, n, cnt):
            # 走過要變成1
            grid[m][n] = 1
            if m == M-1 and n == N-1:
                print(f"m={m}, n={n}")
                nonlocal min_cnt
                min_cnt = min(cnt, min_cnt)
                return
            for d in directions:
                x, y = d[0], d[1]
                if 0 <= m+x < M and 0 <= n+y < N and grid[m+x][n+y] == 0:
                    dfs(m+x, n+y, cnt+1)
        
        dfs(0, 0, 1)
        return min_cnt
        

if __name__ == '__main__':
    print(Solution3().shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(Solution3().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))    
    print(Solution3().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))