import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        透過 Dijkstra's Algorithm 找到距離 k 的所有節點最小距離，若
        有節點的距離仍是 float('inf') 則代表沒有走到。
        """
        # Step 1. Init uni-direction graph
        graph = {}
        for u, v, w in times:
            graph.setdefault(u, []).append((v, w))

        # Step 2. Init heapq and distance
        dist = {i: float("inf") for i in range(1, n+1)}
        dist[k] = 0
        hq = [(0, k)] # (距離, 節點)

        # Step 3. Relaxation
        while hq:
            # 取出 min heap 內距離最小的節點
            d, node = heapq.heappop(hq)
            # 若前往該節點的距離 d 比 dist[node] 還大，那就不用再往下走
            if d > dist[node]:
                continue

            for nei, w in graph.get(node, []):
                # 如果從 node 走到 nei 的距離比現在 dist[nei] 更小
                # 則更新 k -> nei 的最小值
                if d + w < dist[nei]:
                    dist[nei] = d + w
                    heapq.heappush(hq, (dist[nei], nei))

        max_d = max(dist.values())
        return max_d if max_d < float("inf") else -1


# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
res = Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
print(res)