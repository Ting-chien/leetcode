from ast import List
from platform import node
from tkinter import NO
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Step 1. Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2. Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None # Cut the second half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

        # Step 3. Merge two half
        tail = prev
        while tail:
            tmp1, tmp2 = head.next, tail.next
            head.next = tail
            tail.next = tmp1
            head, tail = tmp1, tmp2