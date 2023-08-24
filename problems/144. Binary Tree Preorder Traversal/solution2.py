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
        curr = []
        if not root: return None
        stack = [root]

        while root or stack:
            print(root.val)
            root = stack.pop()
            if root:
                curr.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
            else:
                res += curr

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