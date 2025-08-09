from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        概念上是實作一個在BST中刪除一個節點(key)的算法

        Approach
        1. 比較 root.val 和 key，
            1-1. 若大於則往左側找
            1-2. 若小於則往右側找
        2. 若 root.val == key，比較左右子樹大小
            1-1. 若左右子樹為空，則返回 None
            1-2. 左子樹為空，則返回右子樹
            1-3. 右子樹為空，則返回左子樹
            1-4. 左右子樹都有值，找到右子樹的最小值並替換，接著刪除右子樹的最小值
        """
        if not root: return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root

    def find_min(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        while root.left:
            root = root.left
        return root