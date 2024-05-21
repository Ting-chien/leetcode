from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(node: Optional[TreeNode], path: str):
            nonlocal res
            # return case (if leaf node)
            if not node.left and not node.right:
                res.append(path)
                return
            # general case
            if left := node.left:
                backtrack(left, path + "->" + str(left.val))
            if right := node.right:
                backtrack(right, path + "->" + str(right.val))
        backtrack(root, str(root.val)) # at least one node in tree
        return res
    

def traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + traverse(root.left)
        res = res + traverse(root.right)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(traverse(root))

# Example 1: [1,2,3]
res = Solution().binaryTreePaths(root)
print(res)

# Example 2: [0]
res = Solution().binaryTreePaths(TreeNode(1))
print(res)
