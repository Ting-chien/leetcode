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

class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head: return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)


if __name__ == '__main__':

    def pretty_print(res: Optional[ListNode]):
        while res != None:
            if res.next == None:
                print(res.val)
            else:
                print(res.val, "->", end=" ")
            res = res.next

    # Case 1
    l1 = ListNode(5)
    l1 = l1.add(l1, ListNode(4))
    l1 = l1.add(l1, ListNode(3))
    l1 = l1.add(l1, ListNode(2))
    l1 = l1.add(l1, ListNode(1))
    sol = Solution()
    res = sol.reverseList(l1)
    pretty_print(res)


    # Case 2
    l1 = ListNode(2)
    l1 = l1.add(l1, ListNode(1))
    sol = Solution()
    res = sol.reverseList(l1)
    pretty_print(res)

    # Case 3
    sol = Solution()
    res = sol.reverseList(None)
    pretty_print(res)