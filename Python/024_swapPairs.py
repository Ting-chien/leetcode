from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    '''Iterate'''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        if head and head.next:
            head = head.next
        else:
            return head

        while curr and curr.next:
            tmp = curr.next
            if prev: prev.next = tmp
            curr.next = curr.next.next
            tmp.next = curr
            prev = curr
            curr = curr.next

        return head

class Solution2:
    '''Recursion'''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        next = head.next
        head.next = self.swapPairs(head.next.next)
        next.next = head
        return next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    sol = Solution2()
    res = sol.swapPairs(head=head)
    while res != None:
        if res.next == None:
            print(res.val)
        else:
            print(res.val, "->", end=" ")
        res = res.next