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
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Solution 1. DP(bottom-up)"""
        dp = [None]*(len(cost)+1)
        dp[0], dp[1] = 0, 0
        for i in range(2, len(cost)+1):
            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
            )
        return dp[-1]
        """Solution 2. Optimize space usage from solution 1"""
        a, b = 0, 0
        for i in range(2, len(cost)+1):
            a, b = b, min(
                a + cost[i-2],
                b + cost[i-1]
            )
        return b


# Test 1. 
# Input: cost = [10,15,20]
# Output: 15
print(Solution().minCostClimbingStairs([10,15,20]))

# Test 2.
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))