from typing import List


class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.count = 0

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, start: int, to: int):
        root_s = self.find(start)
        root_t = self.find(to)
        if root_s != root_t:
            self.parents[root_s] = root_t
            if root_t != 0:
                self.count += 1


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        第一次嘗試用 UnionFind，失敗 ❌

        Time: 30:24
        """
        uf = UnionFind(n)
        for start, to in connections:
            uf.union(start, to)
        return uf.count
    

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        問 ChatGPT，透過 DFS 走過有向圖

        Time: 25:36
        """
        # 建立一個 graph 來儲存 cities 之間的連結方向
        graph = [[] for _ in range(n)]
        for u, v in connections:
            # 這裏 (u, v) 代表 u -> v 的方向，而 graph[u] = (v, cost) 代表
            # 從 v -> u 需要的成本
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        # 透過 DFS 從 node 0 開始找尋所有節點，並透過 parent 來紀錄
        # 已經走過的點
        def dfs(node: int, parent: int) -> int:
            count = 0
            for start, cost in graph[node]:
                if start == parent:
                    continue
                count += cost # 從 start -> node 的 cost
                count += dfs(start, node) # 從其他 node -> start 的 cost
            return count
        
        return dfs(0, -1) # 使用 -1 作為 node 0 的 parent

    

# Example 1:
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
res = Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])
print(res)

# Example 2:
# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
res = Solution().minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]])
print(res)

# graph=[[(1,0)], [(0,1), (2,1)], [(1,0), (3,0)], [(2,1), (4,1)], [(3,0)]]
# count=2
# node=0, parent=-1
#     from=1, cost=0, count=0, node=1, parent=0
#         from=0, cost=1, skip
#         from=2, cost=1, count=1, node=2, parent=1
#             from=1, cost=0, skip
#             from=3, cost=0, count=1, node=3, parent=2
#                 from=2, cost=1, skip
#                 from=4, cost=1, count=2, node=4, parent=3
#                     from=3, cosr=0, skip

# Example 3:
# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
res = Solution().minReorder(n = 3, connections = [[1,0],[2,0]])
print(res)