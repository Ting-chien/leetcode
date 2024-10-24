from typing import Optional 

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            if self.flipEquiv(root1.left, root2.left) \
                and self.flipEquiv(root1.right, root2.right):
                return True
            elif self.flipEquiv(root1.left, root2.right) \
                and self.flipEquiv(root1.right, root2.left):
                return True
        return False
    

# Example 1
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
root1 = insert_level_order([1,2,3,4,5,6,None,None,None,7,8])
root2 = insert_level_order([1,3,2,None,6,4,5,None,None,None,None,8,7])
res = Solution().flipEquiv(root1, root2)
print(res)

# Example 2:
# Input: root1 = [], root2 = []
# Output: true
root1 = None
root2 = None
res = Solution().flipEquiv(root1, root2)
print(res)

# Example 3:
# Input: root1 = [], root2 = [1]
# Output: false
root1 = None
root2 = insert_level_order([1])
res = Solution().flipEquiv(root1, root2)
print(res)