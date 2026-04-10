from typing import List, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Find all valid grids that can touch both top-left and bottom-right
        border under the rule of height[A] >= height[B] when going A -> B.

        In reverse, we starting from borders, and check whether we can find
        grids that is height[A] <= height[B] when going A -> B.

        Each time, we start from one grid on the border except for the top-right
        and the bottom-left. Then we run the BFS to travel throught all grids
        on the path until we stocked.

        Time: 2hr
        """

        M, N = len(heights), len(heights[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def bfs(starting: List[Tuple[int]]) -> List[List[int]]:

            if not starting: return []

            visited = set()

            for grid in starting:
                queue = [grid]
                visited.add(grid)
                while queue:
                    cx, cy = queue.pop(0)
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < M and 0 <= ny < N and heights[cx][cy] <= heights[nx][ny] and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))

            return visited
        
        # Find valid grids from top-left border (Pacific Ocean)
        starting = [(i, j) for i in range(M) for j in range(N) if i == 0 or j == 0]
        valid_grids_from_pc = bfs(starting=starting)

        # Find valid grids from bottom-right border (Atlantic Ocean)
        starting = [(i, j) for i in range(M) for j in range(N) if i == M-1 or j == N-1]
        valid_grids_from_ac = bfs(starting=starting)

        # Get intersection of pc and ac
        valid_grids = valid_grids_from_pc & valid_grids_from_ac

        return list(valid_grids)


# Example: 1
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(Solution().pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))