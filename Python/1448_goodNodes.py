from binarytree import build

from utils.binary_tree import insert_level_order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Use DFS to go through all paths from root to leaves, and 
        store current max value in a variable. If node value is greater
        or equal to current max value, add number of good node.

        Complexity
        * Time: O(n)
        * Space: O(n)

        Spend: 36:01
        """
        num_of_good_nodes = 0
        def dfs(node: TreeNode, curr_max: int):
            if not node: return
            # Compare current node value with curr_max
            if node.val >= curr_max:
                nonlocal num_of_good_nodes
                num_of_good_nodes += 1
                curr_max = node.val
            # Go down to subtree of current node
            if node.left:
                dfs(node.left, curr_max)
            if node.right:
                dfs(node.right, curr_max)

        dfs(root, 0)
        return num_of_good_nodes
    

# # Example 1:
# # Input: root = [3,1,4,3,None,1,5]
# # Output: 4
# res = Solution().goodNodes(insert_level_order([3,1,4,3,None,1,5]))
# print(res)

# # Example 2:
# # Input: root = [3,3,null,4,2]
# # Output: 3
# #     3(G,3)
# #    /     \
# #   3(G,3) null
# #  /     \
# # 4(G,4)  2(N,3)
# res = Solution().goodNodes(insert_level_order([3,3,None,4,2]))
# print(res)

# Example 1:
# Input: root = [-1,5,-2,4,4,2,-2,null,null,-4,null,-2,3,null,-2,0,null,-1,null,-3,null,-4,-3,3,null,null,null,null,null,null,null,3,-3]
# Output: 5
res = Solution().goodNodes(insert_level_order([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3]))
print(res)
