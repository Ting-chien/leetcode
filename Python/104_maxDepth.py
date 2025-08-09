from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of the binary tree by BFS.
        
        Args:
            root: Root of the tree
            
        Return:
            Maximum depth of the tree.
        """
        if not root: return 0

        # 建立一個 queue 來儲存每一層的節點，以及使用 ans 來記錄目前的層數
        ans = 0
        q = [[root]]

        # 如果 queue 裡面還有節點的話，那就繼續向下遍歷
        while q:
            nodes = q.pop(0)
            tmp = []
            for node in nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp: q.append(tmp)
            ans += 1

        return ans
    

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of the binary tree by DFS.
        
        Args:
            root: Root of the tree
            
        Return:
            Maximum depth of the tree.
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))