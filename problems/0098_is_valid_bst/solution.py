from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isValidBST(self, root: Optional[TreeNode], left = float('-inf'), right = float('inf')) -> bool:
        """
        Pre-order
        Time: O(n)
        Space: O(n)
        """
        # return if the node is empty
        if not root: return True
        # check if node between left and right, and check left and right subtree
        return left < root.val < right \
            and self.isValidBST(root.left, left, root.val) \
            and self.isValidBST(root.right, root.val, right)
    

class Solution2:
    prev = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """In-order"""
        # 若節點為空，返回 True
        if not root: return True
        # Check left sub tree
        if not self.isValidBST(root.left): return False
        # Check current node
        if root.val <= self.prev: return False
        # Check right sub tree
        self.prev = root.val
        return self.isValidBST(root.right)
    

class Solution3:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Post-order"""
        def bfs(node: Optional[TreeNode]):
            # return (inf, -inf) if empty
            if not node: return float('inf'), float('-inf')
            # get boundary from left and right sub tree
            l_min, l_max = bfs(root.left)
            r_min, r_max = bfs(root.right)
            # check if current node between the boundary
            val = node.val
            if val <= l_max or val >= r_min:
                return float('-inf'), float('inf')
            # return minimum and maximun boundary of the sub tree
            return min(l_min, val), max(r_max, val)
        return bfs(root)[1] != float('inf')



# Example 1
# Input: root = [2,1,3]
# Output: true
root = insert_level_order([2,1,3])
res = Solution3().isValidBST(root)
print(res)

# Example 2
# Input: root = [5,1,4,None,None,3,6]
# Output: false
root = insert_level_order([5,1,4,None,None,3,6])
res = Solution3().isValidBST(root)
print(res)