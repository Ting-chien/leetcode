from typing import List


class Solution:
    cnt = 0
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Transform the tree into a graph
        graph = {}
        for node1, node2 in edges:
            graph.setdefault(node1, []).append(node2)
            graph.setdefault(node2, []).append(node1)
        print(graph)
        # DFS to find the components that can be divided by k 
        self.dfs(0, -1, graph, values, k)
        return self.cnt

    def dfs(self, curr: int, parent: int, graph: dict, values: List[int], k: int):
        print(curr, parent, graph, values, k)
        sum_ = 0
        # 從 undirected tree 的最小 subtree 開始找尋可以被 k 整除的 components
        # 並且返回除以 k 的餘數，來讓 parent node 接續來做計算
        for node in graph[curr]:
            if node != parent:
                sum_ += self.dfs(node, curr, graph, values, k)
                sum_ %= k

        # 將 curr node 的值加入到 sum_ 中
        sum_ += values[curr]
        sum_ %= k

        # 如果 sum_ 為 0，表示可以被 k 整除 
        if sum_ == 0:
            self.cnt += 1

        return sum_


sol = Solution()
res = sol.maxKDivisibleComponents(n = 4, edges = [[0, 1], [1, 2], [1, 3]], values = [10, 10, 10, 10], k = 10)
print(res)