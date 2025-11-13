from typing import List, Any, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + preorder_traverse(root.left)
        res = res + preorder_traverse(root.right)
    return res

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