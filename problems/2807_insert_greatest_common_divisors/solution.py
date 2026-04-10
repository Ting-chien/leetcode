from typing import Optional
from utils.linked_list import insert_nodes, print_nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get gcd
        def _get_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a%b
            return a
        # go through the linked list
        prev, curr = None, head
        while curr:
            if prev:
                gcd = ListNode(val=_get_gcd(prev.val, curr.val))
                prev.next = gcd
                prev.next.next = curr
            prev, curr = curr, curr.next
        return head
    

if __name__ == "__main__":

    # Example 1
    # Input: head = [18,6,10,3]
    # Output: [18,6,6,2,10,1,3]
    head = insert_nodes([18,6,10,3])
    print_nodes(Solution().insertGreatestCommonDivisors(head))

    # Example 2
    # Input: head = [7]
    # Output: [7]
    head = insert_nodes([7])
    print_nodes(Solution().insertGreatestCommonDivisors(head))