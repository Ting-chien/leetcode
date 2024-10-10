from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(head: Optional[TreeNode]) -> int:
            """
            A funtion to get height of a tree, if the tree
            is unbalance, return -1.
            """
            # boundary (leaf node)
            if not head:
                return 0
            # base case, return if tree is unbalance
            l_height = get_height(head.left)
            if l_height == -1: 
                return -1
            r_height = get_height(head.right)
            if r_height == -1:
                return -1
            if abs(l_height - r_height) > 1:
                return -1
            return max(l_height, r_height) + 1
        return get_height(root) != -1
        

# Example 1
# Input: root = [3,9,20,null,null,15,7]
# Output: true
root = insert_level_order([3,9,20,None,None,15,7])
res = Solution().isBalanced(root)
print(res)

# Example 2
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
root = insert_level_order([1,2,2,3,3,None,None,4,4])
res = Solution().isBalanced(root)
print(res)