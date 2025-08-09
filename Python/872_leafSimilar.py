from typing import Optional, List
from utils.binary_tree import insert_level_order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Use DFS to go through tree1 and tree2, and store lead sequences in two list.
        
        Approach
        1. Use DFS to go through tree1 and tree2, and store lead sequences in two list.
        2. Compare if two list are the same
        3. Return True | False

        Complexity
        * Time: O(n1+n2), n1 & n2 are number of nodes in tree1 & tree2
        * Space: O(n1+n2), since nodes might aggregate in one side in worst case (unbalance)
        """

        def dfs(root: Optional[TreeNode], leafs: List[int]) -> List[int]:
            if not root.left and not root.right:
                leafs.append(root.val)
                return leafs
            if root.left:
                dfs(root.left, leafs=leafs)
            if root.right:
                dfs(root.right, leafs=leafs)
            return leafs
        
        leafs1 = dfs(root=root1, leafs=[])
        leafs2 = dfs(root=root2, leafs=[])

        return leafs1 == leafs2


# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: True
root1 = insert_level_order([3,5,1,6,2,9,8,None,None,7,4])
root2 = insert_level_order([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
res = Solution().leafSimilar(root1=root1, root2=root2)
print(res)


# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: True
root1 = insert_level_order([1,2,3])
root2 = insert_level_order([1,3,2])
res = Solution().leafSimilar(root1=root1, root2=root2)
print(res)