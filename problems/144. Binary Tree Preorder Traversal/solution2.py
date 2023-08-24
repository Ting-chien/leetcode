from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return None
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
        

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    sol = Solution()
    print(sol.preorderTraversal(root=root))