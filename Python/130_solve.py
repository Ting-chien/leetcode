from collections import deque
from typing import List, Tuple, Set


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(starting: Tuple[int]) -> Tuple[Set[Tuple[int]], bool]:
            """
            Use a BFS function to find region with cells
            are 'O'.

            Args:
             - starting: Starting cell of region

            Retrun value with be two items
             - region: Cells in region
             - surrounded: Whether the region is surrounded
            """
            # Use a set to store visited cells
            visited = {starting}
            # Put cells we want to visit in queue
            queue = [[starting]]
            # Whether the region is surrounded by 'X'
            surrounded = True

            while queue:
                cells = queue.pop(0)
                next_cells = []
                for cell in cells:
                    for d in directions:
                        next_x = cell[0] + d[0]
                        next_y = cell[1] + d[1]
                        if 0 <= next_x < M and 0 <= next_y < N and board[next_x][next_y] == "O" and (next_x, next_y) not in visited:
                            # Check if region is surrounded
                            if next_x == 0 or next_x == M-1 or next_y == 0 or next_y == N-1:
                                surrounded = False
                            # Walk to next cell
                            visited.add((next_x, next_y))
                            next_cells.append((next_x, next_y))
                if next_cells:
                    queue.append(next_cells)

            return visited, surrounded
        
        # Go through all cell in board except i == 0 or i == M-1 or j == 0 or j == N-1,
        # since we don't need to find region near edge.
        for i in range(1, M-1):
            for j in range(1, N-1):
                if board[i][j] == "O":
                    region, surrounded = bfs(starting=(i, j))
                    # Caputre region if surrounded, if not
                    # use a temorary value "#" to prevent visit twice
                    for m, n in region:
                        board[m][n] = "X" if surrounded else "#"

        # Turn temporary value "#" back to "O"
        for i in range(M):
            for j in range(N):
                if board[i][j] == "#":
                    board[i][j] = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 1. Find all cells on the edge that board[i][j] == "O"
        queue = deque()
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M-1 or j == 0 or j == N-1) and board[i][j] == "O":
                    board[i][j] = "#"
                    queue.append((i, j))

        # Step 2. Find all region that is not surrounded, and replace 
        # cells with a temporary value "#"
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == "O":
                    board[nx][ny] = "#"
                    queue.append((nx, ny))

        # Step 3. Replace all cell in region with "X" or "O". If cell is
        # "#" means not surrounded, otherwise is surrounded
        for i in range(M):
            for j in range(N):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


class Solution:

    parents = []

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parents[py] = px

    def solve(self, board: List[List[str]]) -> None:
        """
        透過 Union Find 算法，將為 "O" 的 cells 合併，若 region 內
        有一 cell 位於邊界，則給定一 dummy head 作為 parent，要注意
        Union Find 是將小樹掛到大樹上，因此 dummy head 的值需要大於
        所有的 cells。
        """
        M, N = len(board), len(board[0])
        self.parents = list(range(M*N+1))
        dummy = M * N
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def get_id(i: int, j: int):
            """
            透過 get_id() 來為 board 上的 cells 賦予一個編號
            """
            return i*N + j

        # 把 board 跑一遍，並將 board[i][j] == "O" 的部分合併
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    if i == 0 or i == M-1 or j == 0 or j == N-1:
                        # 如果 board[i][j] 在邊界，則將其 parent 設為 dummy head
                        self.union(get_id(i, j), dummy)
                    else:
                        for dx, dy in directions:
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == "O":
                                self.union(get_id(i, j), get_id(nx, ny))

        # 將 baord 所有的 cells 檢查一遍，如果 board[i][j] == "O" && 源頭不為 dummy，則
        # 則需要改為 "X"
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    if self.find(get_id(i, j)) != self.find(dummy):
                        board[i][j] = "X"

        print(board)

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]
Solution().solve(board = [["X"]])

# Example 3:
# Input: board = [["O","O","O"],["O","O","O"],["O","O","O"]]]
# Output: [["O","O","O"],["O","O","O"],["O","O","O"]]]
Solution().solve(board = [["O","O","O"],["O","O","O"],["O","O","O"]])

# Example 4:
# Input: board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
# Output: [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
Solution().solve(board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]])
