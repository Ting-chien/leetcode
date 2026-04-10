from typing import Optional
from utils.linked_list import insert_nodes, print_nodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Return if linked list length <= 2
        if not head or not head.next or not head.next.next:
            return head
        
        # Start with node1 and node2, and give them some marks
        odd = prev = head
        even = curr = head.next
        # Use a variable to record length of linked list
        cnt = 2
        # Go through linked list, and move pointer of prev node to node next to curr 
        while curr.next:
            prev.next = curr.next
            prev, curr = curr, curr.next
            cnt += 1

        # After went through whole list, concatenate 
        if cnt % 2 == 1:
            prev.next = None
            curr.next = even
        else:
            prev.next = even

        return odd


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
head = insert_nodes([1,2,3,4,5])
res = Solution().oddEvenList(head=head)
print_nodes(res)

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [1,3,5,2,4,6]
head = insert_nodes([1,2,3,4,5,6])
res = Solution().oddEvenList(head=head)
print_nodes(res)

# Example 3:
# Input: head = []
# Output: []
head = insert_nodes([])
res = Solution().oddEvenList(head=head)
print_nodes(res)

# Example 4:
# Input: head = [1]
# Output: [1]
head = insert_nodes([1])
res = Solution().oddEvenList(head=head)
print_nodes(res)