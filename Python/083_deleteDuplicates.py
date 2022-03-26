from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''Version1'''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

class Solution:
    '''Version2'''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next

        return head

if __name__ == '__main__':
    # Test case1
    # node1 = ListNode(1)
    # node2 = ListNode(1)
    # node3 = ListNode(2)
    # node1.next = node2
    # node2.next = node3
    # Test case2
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    sol = Solution()
    res = sol.deleteDuplicates(None)
    while res != None:
        if res.next == None:
            print(res.val)
        else:
            print(res.val, "->", end=" ")
        res = res.next