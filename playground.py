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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        題目敘述：
        1. 有兩條 linked-list 用來表示兩個非負整數
        2. 數字的顯示方式是倒著排列

        解題思路：

        if I have l1 = [2, 4, 3], l2 = [5, 6, 4]
        means 342 + 465 = 807
        hence result is [7, 0, 8]

        so, we start with the first digit
            2 -> 4 -> 3
          + 5 -> 6 -> 4
        ----------------
          = 7 -> 0 -> 8  
        """
        # set the result linked list
        dummy = curr = ListNode(0)
        tmp = 0
        # go through l1 or l2 if node still exist
        while tmp or l1 or l2:
            # check if l1 can be calculated
            if l1:
                tmp += l1.val
                l1 = l1.next
            # check if l2 can be calculated
            if l2:
                tmp += l2.val
                l2 = l2.next
            # get quotient and remainder
            div, mod = divmod(tmp, 10)
            tmp = div
            curr.next = ListNode(mod)
            curr = curr.next
        
        return dummy.next
    

# Test 1
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Expect Output: [7,0,8]
l1 = insert_nodes([2,4,3])
l2 = insert_nodes([5,6,4])
res = Solution().addTwoNumbers(l1, l2)
print(print_nodes(res))

# Test 2
# Input: l1 = [0], l2 = [0]
# Expect Output: [0]
l1 = insert_nodes([0])
l2 = insert_nodes([0])
res = Solution().addTwoNumbers(l1, l2)
print(print_nodes(res))

# Test 3
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Expect Output: [8,9,9,9,0,0,0,1]
l1 = insert_nodes([9,9,9,9,9,9,9])
l2 = insert_nodes([9,9,9,9])
res = Solution().addTwoNumbers(l1, l2)
print(print_nodes(res))