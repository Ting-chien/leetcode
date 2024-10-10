from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def f(node, cnt):
            """往下遍歷node並透過cnt紀錄現在的深度"""
            if not node: return
            # 紀錄當前的最大深度
            nonlocal res
            cnt += 1
            res = max(res, cnt)
            # 繼續往下遍歷左右子樹
            f(node.left, cnt)
            f(node.right, cnt)
        f(root, 0)
        return res
    

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1