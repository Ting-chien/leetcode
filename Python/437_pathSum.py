from typing import Optional
from utils.binary_tree import insert_level_order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Use DFS + DFS, the first DFS will find all nodes in tree as a 
        start point, the second DFS will add up the value of each path
        start from those start points.

        Approach
        1. Write a DFS function to calculate the sum of the path, and 
        subsctract the value of node each time. If the targetSum become 0,
        it means the path is valid.
        2. Use Dfs to go through all nodes in this tree

        Complexity
        * Time: O(n^2) - beats 22.14%
        * Space: O(2n) - beats 88.09%

        Ref
        * https://blog.csdn.net/fuxuemingzhu/article/details/71097135 
        """
        if not root: return 0
        return self.dfs(root=root, target=targetSum) \
                + self.pathSum(root=root.right, targetSum=targetSum) \
                + self.pathSum(root=root.left, targetSum=targetSum)
        
    def dfs(self, root: Optional[TreeNode], target: int):

        # If path is end
        if not root: return 0

        # Check if path is valid
        num_of_paths = 0
        target -= root.val
        if target == 0:
            num_of_paths += 1

        return num_of_paths \
              + self.dfs(root.left, target) \
              + self.dfs(root.right, target)
            

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Try to use BFS + DFS to solve this question.

        Approach
        1. Traverse all nodes by BFS with a queue
        2. Traverse each node as root add up the path

        Complexity
        * Time: O(n^2) - beats 24.02%
        * Space: O(2n) - beats 70.32%
        """
        if not root: return 0
        queue = [root]

        num_of_paths = 0
        while queue:
            node = queue.pop(0)
            num_of_paths += self.dfs(node, targetSum)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return num_of_paths

        
    def dfs(self, root: Optional[TreeNode], target: int):

        # If path is end
        if not root: return 0

        # Check if path is valid
        num_of_paths = 0
        target -= root.val
        if target == 0:
            num_of_paths += 1

        return num_of_paths \
              + self.dfs(root.left, target) \
              + self.dfs(root.right, target)
    

# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
res = Solution().pathSum(root = insert_level_order([10,5,-3,3,2,None,11,3,-2,None,1]), targetSum = 8)
print(res)

# Example 1:
# Input: root = [1,2,3], targetSum = 8
# Output: 3
res = Solution().pathSum(root = insert_level_order([1,2,3]), targetSum = 8)
print(res)
