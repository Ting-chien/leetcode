from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        # Reverse matrix
        N = len(grid)
        r_grid = [[0]*N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                r_grid[col][row] = grid[row][col]

        # Count appearence of each combination for row and column
        counter = {}
        for comb in grid:
            t_comb = tuple(comb)
            counter[t_comb] = counter.get(t_comb, 0) + 1
        r_counter = {}
        for comb in r_grid:
            t_comb = tuple(comb)
            r_counter[t_comb] = r_counter.get(t_comb, 0) + 1

        # Count pairs
        pairs = 0
        for k, v in counter.items():
            pairs += v * r_counter.get(k, 0)
        
        return pairs


# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
res = Solution().equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])
print(res)

# Example 2:
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
res = Solution().equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
print(res)