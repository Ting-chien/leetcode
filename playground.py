from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
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
# root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
print(traverse(root))

# Test 1: root = [4,2,7,1,3], val = 2
res = Solution().inorderTraversal(root=root)
print(res)

# Test 2: root = [4,2,7,1,3], val = 5
res = Solution().inorderTraversal(root=None)
print(res)

# Test 3: root = 1
res = Solution().inorderTraversal(root=TreeNode(1))
print(res)