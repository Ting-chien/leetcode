from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Related to 257. Binary Tree Paths
    1. Find all possible path from root to leaf
    2. Check if the path sum is equal to the target
    '''
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []
        self.dfs(root=root, path=path, res=res, target=targetSum)
        return res
        
    
    def dfs(self, root: Optional[TreeNode], path: List[int], res: List[List[int]], target: int):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            # Check if all values in path are equal to target
            if sum(path) == target:
                print("Path is {}".format(path))
                res.append(path.copy())
        if root.left:
            self.dfs(root.left, path, res, target)
        if root.right:
            self.dfs(root.right, path, res, target)
        
        path.pop()


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    sol = Solution()
    print(sol.pathSum(root, 22))