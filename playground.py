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
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0
        coins.sort(reverse=True)
        def backtrack(sum: int, remains: List[int]):
            nonlocal count
            if sum == amount:
                count += 1
                return
            for i in range(len(remains)):
                coin = remains[i]
                if coin + sum > amount:
                    continue
                backtrack(coin+sum, remains[i:])
        backtrack(0, coins)
        return count

        records = []
        coins.sort(reverse=True)
        def backtrack(path: List[int], remains: List[int]):
            print(path, remains)
            nonlocal records
            if sum(path) == amount:
                records.append(path[:])
                return
            for i in range(len(remains)):
                coin = remains[i]
                print(f"coin={coin}")
                if coin + sum(path) > amount:
                    continue
                print(i, remains[i:])
                backtrack(path[:]+[coin], remains[i:])
        backtrack([], coins)
        return records


# Test 1. 
# Input: amount = 5, coins = [1,2,5]
# Output: 4
print(Solution().change(amount=5, coins=[1,2,5]))

# Test 2.
# Input: amount = 3, coins = [2]
# Output: 0
print(Solution().change(amount=3, coins=[2]))

# Test 3.
# Input: amount = 10, coins = [10]
# Output: 0
print(Solution().change(amount=10, coins=[10]))