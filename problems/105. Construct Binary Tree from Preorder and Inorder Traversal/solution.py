from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.curr = 0
        self.num_of_nodes = len(preorder)

        def insert(remain: List[int]) -> Optional[TreeNode]:

            if self.curr >= self.num_of_nodes:
                return None
            
            node = TreeNode(preorder[self.curr])
            idx = remain.index(node.val)

            # Left side
            if remain[:idx]:
                self.curr += 1
                node.left = insert(remain=remain[:idx])

            # Right side
            if remain[idx+1:]:
                self.curr += 1
                node.right = insert(remain=remain[idx+1:])

            return node

        return insert(remain=inorder)