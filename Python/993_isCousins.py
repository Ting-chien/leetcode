from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # 透過一 hash map 來紀錄每一層的節點
        d = {}
        # 透過另一 hash map 來紀錄 x, y 的父節點
        r = {}

        def dfs(node, parent, level):
            """
            :TreeNode node: 當前節點
            :TreeNode parent: 父節點
            :int level: 當前節點深度
            """
            if not node:
                return 
            # 紀錄該層的節點
            d.setdefault(level, []).append(node.val)
            # 確認是否為 x 或 y，且非根節點
            if (node.val == x or node.val == y) and parent:
                r[node.val] = parent.val
            # 確認此時是否 x 和 y 都已找到，且兩者根節點不一樣
            if x in d[level] and y in d[level] and r[x] != r[y]:
                return True
            
            return dfs(node.left, node, level+1) or dfs(node.right, node, level+1)

        return True if dfs(root, None, 0) else False

# Example 1
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
root = insert_level_order([1,2,3,4])
res = Solution().isCousins(root=root, x=4, y=3)
print(res)

# Example 2
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
root = insert_level_order([1,2,3,None,4,None,5])
res = Solution().isCousins(root=root, x=5, y=4)
print(res)

# Example 3
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
root = insert_level_order([1,2,3,None,4])
res = Solution().isCousins(root=root, x=2, y=3)
print(res)

# # Example 3
# # Input: root = [5,4,9,1,10,null,7], x = 2, y = 3
# # Output: false
# root = insert_level_order([5,4,9,1,10,None,7])
# res = Solution().isCousins(root=root, x=2, y=3)
# print(res)