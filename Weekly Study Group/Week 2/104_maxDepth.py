from typing import Optional

from tools import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of the binary tree.
        
        Args:
            root: Root of the tree
            
        Return:
            Maximum depth of the tree.
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
res = Solution().maxDepth(root=insert_level_order(arr=[3,9,20,None,None,15,7]))
print(res)