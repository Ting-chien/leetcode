from typing import Optional, List

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [root]
        value = []
        is_even = False
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if left := node.left:
                    queue.append(left)
                if right := node.right:
                    queue.append(right)
            value.append(tmp[::-1] if is_even else tmp) # reverse tmp if even
            is_even = not is_even # reverse the flag every layer
        return value