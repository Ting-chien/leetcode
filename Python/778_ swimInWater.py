from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        1. Use a DFS function to check if we can walk from
        [0,0] to [m-1,n-1], return True if yes.
        2. If not, minus 1 for all elevation of square and 
        try again.
        3. If all elevation in grid are <= 0, return False

        Complexity
         - Time: O(n^4) - TLE
         - Space: O(n^2)
        """
        t = 0 # times cost to walk from top-left to right bottom
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        M, N = len(grid), len(grid[0])
        visited = set()

        def dfs(m: int, n: int) -> bool:
            # Check if it is destination
            if m == M-1 and n == N-1:
                return True
            # Walk four direction
            for d in directions:
                next_x = m + d[0]
                next_y = n + d[1]
                if 0 <= next_x < M \
                    and 0 <= next_y < N \
                    and grid[next_x][next_y] <= 0 \
                    and (next_x, next_y) not in visited:
                    # 如果下一步在框框內、可走、還沒走過，那就走
                    visited.add((next_x, next_y))
                    is_reachable = dfs(next_x, next_y)
                    if is_reachable: return True
                    visited.remove((next_x, next_y))

        def not_submerged():
            # 這裡不包含 == 的原因，是因為當地一次都被雨水覆蓋時，希望可以再檢查一次
            # 路線是否通
            flag = not all([grid[m][n] < 0 for m in range(M) for n in range(N)])
            return flag

        # If the grid is not been submerged yet, we can try again
        # However, if the grid is submerged still not reachable, 
        # return False
        while not_submerged():
            # 從(0,0)開始走
            if grid[0][0] <= 0:
                starting = (0, 0)
                visited.add(starting)
                is_reachable = dfs(0, 0)
                if is_reachable: return t
                visited.remove(starting)
            # 這次走失敗，則雨水深度 -1
            for m in range(M):
                for n in range(N):
                    grid[m][n] -= 1
            t += 1

        return -1
    

# Example 1:
# Input: grid = [[0,2],[1,3]]
# Output: 3
res = Solution().swimInWater(grid = [[0,2],[1,3]])
print(res)

# Example 2:
# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
res = Solution().swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
print(res)

# Example 3:
# Input: grid = [[3,2],[0,1]]
# Output: 3
res = Solution().swimInWater(grid = [[3,2],[0,1]])
print(res)
