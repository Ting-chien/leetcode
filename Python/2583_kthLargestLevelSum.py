from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        stack = [root]
        while stack:
            tmp = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                if left := node.left:
                    stack.append(left)
                if right := node.right:
                    stack.append(right)
            res.append(sum(tmp))
        return -1 if k > len(res) else sorted(res, reverse=True)[k-1]