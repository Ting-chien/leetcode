from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"ListNoe(val={self.val})"
    def add(self, curNode, addNode):
        addNode.next = curNode
        curNode = addNode
        return curNode

# 再實作指反轉特定範圍的 linked list function
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. Make a dummy head, and find the start point of reversion
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head
        for _ in range(left-1):
            leftPrev, curr = curr, curr.next

        # 2. Reverse nodes
        prev = None
        for _ in range(right-left+1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        # 3. Concat head and tail to reverse nodes
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next
        

if __name__ == '__main__':

    def pretty_print(head: Optional[ListNode]):
        while head != None:
            if head.next == None:
                print(head.val)
            else:
                print(head.val, "->", end=" ")
            head = head.next

    # Case 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    pretty_print(head)
    sol = Solution()
    res = sol.reverseBetween(head, left=2, right=4)
    pretty_print(res)


    # # Case 2
    l1 = ListNode(5)
    sol = Solution()
    res = sol.reverseBetween(l1, left=1, right=1)
    pretty_print(res)