from typing import List, Optional
from collections import defaultdict

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """Time Limit Exceed"""
        def get_depth(node: Optional[TreeNode], edge: int):
            """
            Function get_depth() is used to get the
            depth of a binary tree.

            :param node: Root of binary tree
            :param edge: Value of which node should return
            """
            if not node or node.val == edge:
                return 0
            return max(get_depth(node.left, edge), get_depth(node.right, edge)) + 1
        res = []
        for q in queries:
            res.append(get_depth(node=root, edge=q)-1)
        return res
    

class Solution2:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        # get depth of each nodes to their leaf
        d = {}
        def get_depth(node: Optional[TreeNode]):
            """
            Get depth of each subtree of nodes

            :param node: Root of binary tree
            """
            if not node:
                return 0
            depth = max(get_depth(node.left), get_depth(node.right)) + 1
            d[node.val] = depth
            return depth
        get_depth(node=root)
        
        # check visibility of each nodes
        res = [0] * (len(d)+1)
        def get_visible_depth(node, depth, visible_depth):
            if not node:
                return
            # 將當下節點在二叉樹中的可視最深深度儲存起來
            res[node.val] = depth + visible_depth
            # 往下繼續遍歷左、右子樹
            get_visible_depth(node.left, depth+1, d[node.right])
        
    

# Example 1
# Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
# Output: [2]
root = insert_level_order([1,3,4,2,None,6,5,None,None,None,None,None,7])
res = Solution2().treeQueries(root=root, queries=[4])
print(res)

# Example 2
# Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
# Output: [3,2,3,2]
root = insert_level_order([5,8,9,2,1,3,7,4,6])
res = Solution2().treeQueries(root=root, queries=[3,2,4,8])
print(res)