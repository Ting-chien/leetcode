from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """透過迭代的方式找尋 binary tree 的 paths，和一般
        作法不同的地方是，stack 除了會儲存 node 外，還會保留
        當時的路徑紀錄。
        """
        if not root: return
        stack = [(root, str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            # insert path into res if lead node
            if not node.left and not node.right:
                res.append(path)
            # go throught left and right sub tree
            if right := node.right:
                stack.append((right, path + "->" + str(right.val)))
            if left := node.left:
                stack.append((left, path + "->" + str(left.val)))
        return res
    

def traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + traverse(root.left)
        res = res + traverse(root.right)
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(traverse(root))

# Test 1: root = [4,2,7,1,3], val = 2
res = Solution().levelOrder(root=root)
print(res)

# Test 2: root = [4,2,7,1,3], val = 5
res = Solution().levelOrder(root=None)
print(res)

# Test 3: root = 1
res = Solution().levelOrder(root=TreeNode(1))
print(res)