from typing import Optional, List, Any


# Definition for a binary tree node.
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
    if not arr or not arr[0]: return None
    if len(arr) <= 1: return TreeNode(arr[0])
    
    root = TreeNode(arr[0])
    i = 1
    queue = [root]

    while i < len(arr):
        curr = queue.pop(0)
        # 插入左子節點
        curr.left = TreeNode(arr[i]) if arr[i] else None
        if arr[i]:
            queue.append(curr.left)
        i += 1
        # 插入右子節點
        if i < len(arr):
            curr.right = TreeNode(arr[i]) if arr[i] else None
            if arr[i]:
                queue.append(curr.right)
        i += 1
    
    return root


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """使用 stack 解決問題，在 stack 中同時儲存 (node, path, curr_sum)"""
        if not root: return 
        res = []
        stack = [(root, [root.val], root.val)]
        while stack:
            node, path, tmp = stack.pop()
            if not node.left and not node.right and tmp == targetSum:
                res.append(path[:])
            if left := node.left:
                stack.append((left, path+[left.val], tmp+left.val))
            if right := node.right:
                stack.append((right, path+[right.val], tmp+right.val))
        return res

