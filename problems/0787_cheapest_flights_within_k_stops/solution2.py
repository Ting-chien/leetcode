import heapq
from tracemalloc import stop
from typing import List
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Cost
        cost = [float('inf')] * n
        cost[src] = 0

        # Do k+1 times relaxation for stop k times
        for _ in range(k+1):
            prev = cost.copy()
            for u, v, w in flights:
                if prev[u] != float('inf'):
                    cost[v] = min(cost[v], prev[u] + w)

        return cost[dst] if cost[dst] != float('inf') else -1


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3, k=1))  # 700

    # Test cases 2
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))  # 200

    # Test cases 3
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))  # 500
