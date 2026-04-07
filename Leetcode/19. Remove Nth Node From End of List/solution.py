from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(l: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for i in range(len(l)):
        node = ListNode(l[i])
        curr.next = node
        curr = curr.next
    return dummy.next

def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Use recrusive to find the nth node in the list"""

        # Add a dummy head in case only 1 node in the list
        dummy = ListNode(0)
        dummy.next = head

        def recursive(cnt: int, prev: Optional[ListNode], curr: Optional[ListNode]):
            # Return if we find all nodes already
            if curr == None:
                return 0
            # Update count from the tail
            cnt = recursive(cnt, curr, curr.next) + 1
            # Connect prev and next node 
            if cnt == n:
                prev.next = curr.next
            return cnt

        recursive(0, dummy, dummy.next)
        return dummy.next


# Test 1
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
head = create_list([1,2,3,4,5])
n = 2
print_list(Solution().removeNthFromEnd(head, n))


# Test 2
# Input: head = [1], n = 1
# Output: []
head = create_list([1])
n = 1
print_list(Solution().removeNthFromEnd(head, n))