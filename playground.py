from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """If you want to print your node in level order, it is like 
        a BFS and I'm going to go though all these nodes with a queue.
        """
        if not root: return
        queue = [root, None]
        value = []
        while queue != [None]:
            tmp = []
            while queue:
                node = queue.pop(0)
                if node:
                    tmp.append(node.val)
                    if left := node.left:
                        queue.append(left)
                    if right := node.right:
                        queue.append(right)
                else:
                    break
            value.append(tmp)
            queue.append(None)
        return value
    

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