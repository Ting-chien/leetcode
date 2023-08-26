from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = {}
        stack = [{"level": 0, "node": root}]

        while stack:
            d = stack.pop()
            level = d["level"]
            node = d["node"]
            # Set node val into res
            res.setdefault(level, [])
            res[level].append(node.val)
            if node.left:
                stack.append({"level": level+1, "node": node.left})
            if node.right:
                stack.append({"level": level+1, "node": node.right})

        return [res[i] for i in res]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.levelOrder(root=root))