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
    def isPalindrome(self, s: str) -> bool:
        """
        解題路線：
        1. 移除非英數字的部分
        2. 將所有字符轉成小寫
        3. 透過左右兩隻指針，檢查是否所有遍歷過程中遇到的字符都一樣
        """
        # remove non-alphanumeric and turn string into lowercase
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()

        # iterate s by left and right pointer, and check if s
        # is a palindrome
        l_p = 0
        r_p = len(s)-1
        while l_p < r_p:
            if s[l_p] != s[r_p]: return False
            l_p += 1
            r_p -= 1

        return True


# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))

# Example 2:
# Input: s = "race a car"
# Output: false
print(Solution().isPalindrome(s="race a car"))

# Example 3:
# Input: s = " "
# Output: true
print(Solution().isPalindrome(s=" "))