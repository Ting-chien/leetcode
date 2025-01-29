from typing import List
from collections import defaultdict


class Solution:

    def is_connected(self, source: int, target: int, visited: set, graph: dict) -> bool:
        """
        透過 DFS 檢查 source 和 target 之間是否相連
        
        Args:
            source: 起始節點
            target: 目標節點
            visited: 儲存走過的節點
            graph: 儲存所有節點的關聯
        """
        # 如果 source 和 target 一樣，則代表可相連
        if source == target:
            return True
        # 若不一樣，往下繼續查找
        visited.add(source)
        for adjacent in graph[source]:
            # 若 adjacent 尚未走過，且可以連到 target，則代表可以連到
            if adjacent not in visited and self.is_connected(adjacent, target, visited, graph):
                return True
        return False
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Intuition: 
        1. 將所有的 node 和其關聯存於 map `graph` 裡
        2. 遍歷 edges，如果兩個 nodes 都和其他 node 有連結，則檢查這兩個 nodes 是否也相連
        3. 透過 dfs 檢查 source node 是否可以連到 target node (透過 visited 避免無限遞迴)
        """
        # 宣告一 hash map 來儲存 nodes 之間的關離
        graph = defaultdict(set)
        # 遍歷所有的 edge
        for node1, node2 in edges:
            # 如果 node1, node2 都已有連結過，則檢查是否相連
            if node1 in graph and node2 in graph and self.is_connected(node1, node2, set(), graph):
                return [node1, node2]
            # 如果還沒，則先建立連結
            graph[node1].add(node2)
            graph[node2].add(node1)


# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]

# 1. Use graph to represent the connection between nodes

# Round 1. 
# * u=1, v=2
# * graph = {1: [2], 2: [1]}

# Round 2.
# * u=1, v=3
# * graph = {1: [2, 3], 2: [1], 3: [1]}

# Round 3.
# * u=2, v=3
# * check dfs function
#     - node = 2, target = 3, visited = set()
#     - visited = {2}
#     - for neighbor in graph[2] = [1]
#     - neighbor = 1 and 1 not in visited
#         - check dfs(1, 3, {2})
#             - node = 1, target = 3, visited = {2}
#             - visited = {1, 2}
#             - for neighbor in graph[1] = [2, 3]
#             - neighbor = 2 and 2 in visited, continue
#             - neighbor = 3 and 3 not in visited
#                 - check dfs(3, 3, {1, 2})
#                     - node = 3, target = 3, visited = {1, 2}
#                     - return True
#         - return True
# * return [2, 3]