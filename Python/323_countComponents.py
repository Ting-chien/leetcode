from typing import List
from collections import defaultdict


class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            # 代表已經在同一個 component 內
            if root_x == root_y:
                return 0
            # 這裡使用 max heap 將較大的值放於上方
            if rank[root_y] > rank[root_x]:
                parent[root_x] = root_y
                rank[root_y] += rank[root_x]
            else:
                parent[root_y] = root_x
                rank[root_x] += rank[root_y]
            return 1 # 合併加一
        
        res = n
        for x, y in edges:
            # 遍歷所有邊界關係，若可以合併則代表少掉一個 conntect componets
            res -= union(x, y)
        print(parent)
        return res


class UnionFind:
    def __init__(self, n):
        # 初始每個節點都是一個 connected component
        self.parent = list(range(n))
        self.count = n  

    def find(self, x):
        """透過 find() 函數，找到 x 節點的根節點"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路徑壓縮
        return self.parent[x]

    def union(self, x, y):
        """透過 union() 函數，將 x, y 節點所屬的樹合併"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.count -= 1  # 每 union 成功一次，就少一個分量

class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        print(uf.parent)
        return uf.count


# # Example 1:
# # Input: n=3, edges=[[0,1], [0,2]]
# # Output:1
# ans = Solution().countComponents(n=3, edges=[[0,1], [0,2]])
# print(ans)

# # Example 2:
# # Input: n=6, edges=[[0,1], [1,2], [2,3], [4,5]]
# # Output: 2
# ans = Solution().countComponents(n=6, edges=[[0,1], [1,2], [2,3], [4,5]])
# print(ans)

# Example 3:
# Input: n=6, edges=[[0, 1], [2, 3], [4, 5], [0, 2], [0, 4]]
# Output: 
res1 = Solution1().countComponents(n=6, edges=[[0, 1], [2, 3], [4, 5], [0, 2], [4, 0]])
res2 = Solution2().countComponents(n=6, edges=[[0, 1], [2, 3], [4, 5], [0, 2], [4, 0]])