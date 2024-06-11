from typing import Optional, List, Any


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_nodes(arr: List[Any]) -> Optional[ListNode]:
    dummy = curr = ListNode(0)
    for ele in arr:
        curr.next = ListNode(ele)
        curr = curr.next
    return dummy.next

def print_nodes(node: Optional[ListNode]) -> List[Any]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

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
    # def uniquePaths(self, m: int, n: int) -> int:
    #     """
    #     透過二維的陣列dp[m+1][n+1]來實作動態規劃，將每一格可走到的方法數
    #     由dp[i][j-1]+dp[i-1][j]來求得。
    #     """
    #     dp = [[0]*(n+1)]*(m+1)
    #     dp[1][1] = 1
    #     for i in range(1,m+1):
    #         for j in range(1,n+1):
    #             dp[i][j] = dp[i][j-1] + dp[i-1][j]
    #     print(dp)
    #     return dp[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(col: int, row: int):
            nonlocal m, n
            if col == m-1 or row == n-1:
                return 1
            return dp(col+1, row) + dp(col, row+1)
        return dp(0, 0)


# Test 1. 
# Input: m = 3, n = 7
# Output: 28
print(Solution().uniquePaths(m=3, n=7))

# Test 2.
# Input: m = 3, n = 2
# Output: 3
print(Solution().uniquePaths(m=3, n=2))