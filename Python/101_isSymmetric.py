from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSymmetricTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check if two tree are symmetric"""
        # boundary
        if not p or not q:
            # check if q and q are empty
            return p is q
        # base case
        return p.val == q.val \
            and self.isSymmetricTree(p.left, q.right) \
            and self.isSymmetricTree(p.right, q.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check if a tree is symmetric"""
        return self.isSymmetricTree(root.left, root.right)
    

# Example 1
# Input: root = [1,2,2,3,4,4,3]
# Output: true
root = insert_level_order(arr=[1,2,2,3,4,4,3])
res = Solution().isSymmetric(root=root)
print(res)

# Example 2
# Input: root = [1,2,2,null,3,null,3]
# Output: false
root = insert_level_order(arr=[1,2,2,None,3,None,3])
res = Solution().isSymmetric(root=root)
print(res)