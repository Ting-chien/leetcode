from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float('-inf')
        def dfs(root: Optional[TreeNode]) -> int:

            nonlocal max_sum

            # Condition
            if not root: return 0

            # Recursive
            left_sum = dfs(root=root.left)
            right_sum = dfs(root=root.right)

            # Do the math
            if left_sum < 0: left_sum = 0
            if right_sum < 0: right_sum = 0

            sum = root.val+left_sum+right_sum
            max_sum = max(max_sum, sum)
            return max(root.val+left_sum, root.val+right_sum)

        dfs(root=root)
        return max_sum
        

if __name__ == '__main__':

    # Case1
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)

    # Case2
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxPathSum(root=root))