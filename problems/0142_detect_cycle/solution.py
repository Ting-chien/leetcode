from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # remove one node linked-list
        if not head or not head.next: return None

        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast: return None
            slow = slow.next
            fast = fast.next.next

        count = 0
        while head != slow:
            head = head.next
            slow = slow.next
            count += 1

        return count

if __name__ == '__main__':
    # node1 = ListNode(3)
    # node2 = ListNode(2)
    # node3 = ListNode(0)
    # node4 = ListNode(-4)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node2
    # sol = Solution()
    # print(sol.detectCycle(node1))
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    # node2.next = node1
    sol = Solution()
    print(sol.detectCycle(node1))
    # node1 = ListNode(1)
    # sol = Solution()
    # print(sol.detectCycle(node1))