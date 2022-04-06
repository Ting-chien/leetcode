from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        curr = root
        while stack or curr:
            # Traverse in inorder way(left node first)
            while curr:
                stack.append(curr)
                curr = curr.left
            # Back to the parent node and traverse to right node
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.right = node2
    node2.left = node3
    sol = Solution2()
    print(sol.inorderTraversal(root))