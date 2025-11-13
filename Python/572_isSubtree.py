from typing import Optional
from utils.binary_tree import insert_level_order, print_tree_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Check whether two trees are the same"""
        if not root1 or not root2:
            return root1 == root2
        return root1.val == root2.val \
            and self.isSameTree(root1.left, root2.left) \
            and self.isSameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Check whether subRoot is root's subtree"""
        if not root: return False
        # Start comparing two trees when root node is equal
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        # If not, compare left and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

class Solution:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        return f"^{root.val} {self.serialize(root.left)} {self.serialize(root.right)}"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.serialize(subRoot) in self.serialize(root)
    

class Solution:
    def isSubtree(self, root, subRoot):
        def hashTree(node):
            if not node: return "#"
            return f"{node.val},{hashTree(node.left)},{hashTree(node.right)}"
        return hashTree(subRoot) in hashTree(root)


# Example 1:
# root1 = insert_level_order([1,2,3])
# root2 = insert_level_order([1,2,4])
# print(Solution().isSameTree(root1, root2))

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
print(Solution().isSubtree(root=insert_level_order([3,4,5,1,2]), subRoot=insert_level_order([4,1,2])))

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: true
print(Solution().isSubtree(root=insert_level_order([3,4,5,1,2,None,None,None,None,0]), subRoot=insert_level_order([4,1,2])))