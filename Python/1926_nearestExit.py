from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        使用BFS去往所在位置的四周走去，遇到'+'就不能走，如果在邊界則代表找到出口。

        Approach
        1. Use a queue to store the valid steps (not '+' and inside maze)
        2. Use another variable steps to count how many steps to escape
        3. Since you can not escape from initilzie place (steps != 0), so return -1 if steps is 0
        4. For every time, put valid steps into queue
        """
        steps = -1
        queue = [[entrance]]
        M, N = len(maze), len(maze[0])
        exit = False
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            places = queue.pop(0)
            next_places = []
            steps += 1
            for p in places:
                # Find exit
                if (p[0] == 0 or p[0] == M-1 or p[1] == 0 or p[1] == N-1) and p != entrance:
                    return steps
                # Go up, down, left, right
                for d in directions:
                    next_row = p[0] + d[0]
                    next_col = p[1] + d[1]
                    # print(f"[{next_row}, {next_col}]")
                    if 0 <= next_row < M and 0 <= next_col < N and maze[next_row][next_col] != "+":
                        maze[next_row][next_col] = "+"
                        next_places.append([next_row, next_col])
            if next_places: queue.append(next_places)

        return -1
    

# Example 1:
# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
res = Solution().nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2])
print(res)

# Example 2:
# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
res = Solution().nearestExit( maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0])
print(res)

# Example 3:
# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
res = Solution().nearestExit(maze = [[".","+"]], entrance = [0,0])
print(res)