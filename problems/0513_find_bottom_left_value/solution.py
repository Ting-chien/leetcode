from typing import Optional, List

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            # go through right node and then left node
            if right := node.right:
                queue.append(right)
            if left := node.left:
                queue.append(left)
        return node.val # return last node 