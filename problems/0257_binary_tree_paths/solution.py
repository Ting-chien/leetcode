from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root: return []

        res = []
        self.traverse(root, "", res)
        return res

    def traverse(self, root: TreeNode, s: str, res: List[str]) -> None:
        if not root.left and not root.right:
            res.append(s + str(root.val))
        else:
            tmp = s + str(root.val) + "->"
            if root.left: self.traverse(root.left, tmp, res)
            if root.right: self.traverse(root.right, tmp, res)

class Solution2:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root: return []

        res = []
        self.backtrack(root, [], res)
        return res

    def backtrack(self, root: TreeNode, path: List[str] = [], res: List[str] = []) -> None:

        if not root.left and not root.right:
            path.append(str(root.val))
            res.append("->".join(path))
            path.pop()
        
        path.append(str(root.val))
        if root.left: self.backtrack(root.left, path, res)
        if root.right: self.backtrack(root.right, path, res)
        path.pop()

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    sol = Solution2()
    print(sol.binaryTreePaths(root=root))