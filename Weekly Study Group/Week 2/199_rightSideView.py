from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Find all visible nodes from the right side.
        
        Args:
            root: Root of tree
            
        Return:
            All visible nodes
        """
        # Store answer if an array
        res = []
        # Traverse nodes by DFS
        def dfs(root: Optional[TreeNode], depth: int):
            # Empty node
            if not root: return
            # Append node to answer if depth >= len(ans)
            if depth >= len(res):
                res.append(root.val)
            # Check from the right side, then left side
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        dfs(root, 0)
        return res