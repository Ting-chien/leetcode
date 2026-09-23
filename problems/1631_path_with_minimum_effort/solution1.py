import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        M, N = len(heights), len(heights[0])
        efforts = [[float('inf')] * N for _ in range(M)]
        efforts[0][0] = 0
        hq = [(0, (0, 0))] # (effort, node)

        while hq:

            effort, node = heapq.heappop(hq)
            m, n = node[0], node[1]

            # Skip if current path effor is larger than the best case to node
            if effort > efforts[m][n]:
                continue

            # Find adjacent fields
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = m+dx, n+dy
                if 0 <= nx < M and 0 <= ny < N:
                    new_effort = max(effort, abs(heights[nx][ny] - heights[m][n]))
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(hq, (new_effort, (nx, ny)))

        return efforts[M-1][N-1]


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print(solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2

    # Example 2
    print(solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # 1

    # Example 3
    print(
        solution.minimumEffortPath(
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ]
        )
    )  # 0
