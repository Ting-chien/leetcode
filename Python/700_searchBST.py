from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            # Check whether node value equal to target value here
            if root.val == val: return root
            # if not, check next node in pre-order way.
            return self.searchBST(root.left, val) or self.searchBST(root.right, val)
    
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        善用 BST 的特性，左子樹 < root value < 右子樹來節省遍歷的次數
        """
        if not root:
            return root
        elif root.val==val:
            return root
        elif root.val<val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left,val)

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