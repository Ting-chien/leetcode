from typing import List, Optional
from utils.binary_tree import insert_level_order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        透過遞迴的方式計算左、右子樹的深度，並返回最大的深度，同時將佐、右
        子樹的深度相加來代表當前 vertex 的 diameter，並跑過所有的 vertex
        來找到最大的 diameter。

        Complexity
        * Time: 跑過所有 vertex 一次 O(n)
        * Space: 不平衡樹 O(n)
        """

        # 當前最大直徑
        diameter = 0

        def traverse(node: Optional[TreeNode]):

            # 如果當前節點不存在則返回
            if not node:
                return -1
            
            # 取得左、右子樹的深度
            left_d = traverse(node.left) + 1
            right_d = traverse(node.right) + 1
            # print(f"Current vertex: {node.val}")
            # print(f"Depth of left side: {left_d}")
            # print(f"Depth of right side: {right_d}")

            # 計算當前直徑
            nonlocal diameter
            diameter = max(diameter, (left_d+right_d))
            # print(f"Current diameter = {diameter}")

            return max(left_d, right_d)
        
        traverse(node=root)
        return diameter
    

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
root = insert_level_order(arr=[1,2,3,4,5])
res = Solution().diameterOfBinaryTree(root=root)
print(res)

# Example 2:
# Input: root = [1,2]
# Output: 1
root = insert_level_order(arr=[1,2])
res = Solution().diameterOfBinaryTree(root=root)
print(res)

# Example 3:
# Input: root = [1,2,3,4,5,None,None,7, None, 8, None, ]
# Output: 1
# root = insert_level_order(arr=[1,2,3,4,5,None,None,7, None, 8, None, None,None,None,None,None,None,10])
# res = Solution().diameterOfBinaryTree(root=root)
# print(res)