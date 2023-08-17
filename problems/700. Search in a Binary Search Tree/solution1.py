from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(root: Optional[TreeNode]):
            if root:
                if root.val == val: return root
                if left := traverse(root=root.left):
                    return left
                if right := traverse(root=root.right):
                    return right
        return traverse(root=root)

if __name__ == '__main__':
    node1 = TreeNode(val=4)
    node1.left = TreeNode(val=2)
    node1.right = TreeNode(val=7)
    node1.left.left = TreeNode(val=1)
    node1.left.right = TreeNode(val=3)

    sol = Solution()
    res = sol.searchBST(root=node1, val=2)
    print(res.val)
    print(res.left.val)
    print(res.right.val)