from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        if root:
            res.append(root.val)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)

        return res
        

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    print(sol.preorderTraversal(root=root))