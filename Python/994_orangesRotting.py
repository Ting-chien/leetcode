from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Use BFS to expand rotting, and store rotten orange in
        this minute in a queue. If next place is empty or the
        oragne is alreaady rotten, ignore it.

        Find if there is fresh orange once expand is over.
        """
        minutes = -1
        M, N = len(grid), len(grid[0])
        queue = [[[row, col] for row in range(M) for col in range(N) if grid[row][col] == 2]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            minutes += 1
            rotten_oranges = queue.pop(0)
            next_rotten_oranges = []
            for ro in rotten_oranges:
                for d in directions:
                    next_row = ro[0] + d[0]
                    next_col = ro[1] + d[1]
                    if 0 <= next_row < M and 0 <= next_col < N and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        next_rotten_oranges.append([next_row, next_col])
            if next_rotten_oranges: queue.append(next_rotten_oranges)

        # Check if there is fresh orange
        return minutes if all([grid[row][col] != 1 for row in range(M) for col in range(N)]) else -1
    

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
res = Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]])
print(res)

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
res = Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]])
print(res)


# [
#     [2,2,2],
#     [0,2,2],
#     [1,0,2]
# ]

# queue = [[[0,0]]], minutes = 0
# queue = [[[0,1]]], minutes = 1
