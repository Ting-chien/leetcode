import heapq
from typing import List


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         """
#         Double for-loop
#         Time: O(n^)
#         Space: O(n)

#         ❌: 會重複計算到多個點之間的距離
#         """
#         min_cost = 0
#         for i in range(len(points)):
#             src = points[i]
#             dst_points = points[:i] + points[i+1:]
#             options = []
#             for j in range(len(dst_points)):
#                 dst = dst_points[j]
#                 options.append((abs(src[0]-dst[0]) + abs(src[1]-dst[1])))
#             min_val = min(options)
#             print(f"Min cost from {src} took {min_val}")
#             min_cost += min(options)
#         return min_cost
    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Min Spanning Tree(MST) - Prim's Algorithm
        Time: O(n^2 + log(n))
        """
        N = len(points)

        # 建立一個 graph 紀錄每一個點，到其他所有點的 cost [cost, item]
        # 雙迴圈的時間複雜度是 O(n^2)
        graph = {i: [] for i in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        # Prim's Algorithm，每次取出 為走訪過 且 cost最小 的點
        # Heap 每次取出的時間複雜度為 O(logn)
        min_cost = 0 # 最小 cost 總和
        visited = set() # 紀錄走過的點
        min_h = [[0, 0]] # 從 [0,0] 開始，因為第一個點和自己重疊
        while len(visited) < N:
            cost, vertex = heapq.heappop(min_h)
            if vertex in visited:
                continue
            min_cost += cost
            visited.add(vertex)
            for cost, neighbor in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_h, [cost, neighbor])
        
        return min_cost
    

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
ans = Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])
print(ans)
