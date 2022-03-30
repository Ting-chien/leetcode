from turtle import right
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True

        if p and q:
            if (self.isSameTree(p.left, q.left) and
                p.val == q.val and
                self.isSameTree(p.right, q.right)):
                return True

        return False

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(3)
    q.right = TreeNode(2)
    sol = Solution()
    print(sol.isSameTree(p, q))