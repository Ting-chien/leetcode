from typing import Optional

from utils.linked_list import insert_nodes, print_nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Intuition: 透過遞迴往下尋找直到走到 list 的尾端，當遇到尾端時開始
        返回當前的 node，但若當前的位置是 N-n+1 則要返回前一個 node。
        """
        target = None # Target position we want to remove

        def dfs(i: int, node: Optional[ListNode]) -> Optional[ListNode]:
            # Base case (meet the end of list)
            if not node:
                nonlocal target
                target = i - n
                return None
            # General case
            prev = dfs(i+1, node.next)
            if i == target:
                return prev
            node.next = prev
            return node
        
        new_head = dfs(1, head)
        return new_head
    

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
head = insert_nodes([1,2,3,4,5])
res = Solution().removeNthFromEnd(head = head, n = 2)
print_nodes(res)