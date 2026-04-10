from typing import Optional, List, Any
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_level_order(arr: List[Any]) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1  # index in arr

    while queue and i < len(arr):
        node = queue.popleft()

        # 左子節點
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # 右子節點
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

def print_tree_level_order(root: Optional[TreeNode]):
    if not root:
        print("Empty tree")
        return
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    print(res)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Intuition: Use recursive to travel down to the leaf and swich left
        and right node from their parents.

        Complexity
         - Time: O(n), n is number of nodes in the tree
         - Space: O(1)
        """

        if not root: return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """BFS"""

        if not root: return None

        queue = deque([root])

        while queue:

            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


# Example 1
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
root = insert_level_order([4,2,7,1,3,6,9])
res = Solution().invertTree(root=root)
print_tree_level_order(res)

# Example 2
# Input: root = [2,1,3]
# Output: [2,3,1]
root = insert_level_order([2,1,3])
res = Solution().invertTree(root=root)
print_tree_level_order(res)