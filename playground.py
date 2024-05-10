from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        概念：此題想透過pre-order的方式往下查找BST中符合條件的node，當遇到node的值等於val時，
        直接將node回傳，若不等於則以遞迴的方式往左或右查找，若沒有左或右節點則回傳null。
        """
        if root:
            # Check whether node value equal to target value here
            if root.val == val: return root
            # if not, check next node in pre-order way.
            return self.searchBST(root.left, val) or self.searchBST(root.right, val)
        
        return None
    

def traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + traverse(root.left)
        res = res + traverse(root.right)
    return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(traverse(root))

# Test 1: root = [4,2,7,1,3], val = 2
res = Solution().searchBST(root, val=2)
print(traverse(res))

# Test 2: root = [4,2,7,1,3], val = 5
res = Solution().searchBST(root, val=5)
print(traverse(res))