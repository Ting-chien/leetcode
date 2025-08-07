from typing import Optional
from utils.linked_list import insert_nodes, print_nodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Return if length == 1
        if not head or not head.next:
            return head
        
        # Get length of linked-list
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        # Iterate to the middle node
        middle = N // 2
        step, prev, curr = 0, None, head
        while curr:
            if step == middle:
                prev.next = curr.next
                break
            step += 1
            prev, curr = curr, curr.next

        return head
    

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Return if length == 1
        if not head or not head.next:
            return None
        
        # Use slow and fast pointers to find middle and last position at
        # the same time
        slow = fast = head
        step = 0
        while fast.next and fast.next.next:
            if step % 2 == 1:
                slow = slow.next
            fast = fast.next
            step += 1

        # Remove middle node
        slow.next = slow.next.next

        return head


# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
h = insert_nodes([1,3,4,7,1,2,6])
res = Solution().deleteMiddle(h)
print_nodes(res)

# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
h = insert_nodes([1,2,3,4])
res = Solution().deleteMiddle(h)
print_nodes(res)

# Example 3:
# Input: head = [2,1]
# Output: [2]
h = insert_nodes([2,1])
res = Solution().deleteMiddle(h)
print_nodes(res)

# Example 3:
# Input: head = [2]
# Output: []
h = insert_nodes([2])
res = Solution().deleteMiddle(h)
print_nodes(res)

# Example 5:
# Input: head = [1,3,4,7,1,2,]
# Output: [1,3,4,1,2]
h = insert_nodes([1,3,4,7,1,2])
res = Solution().deleteMiddle(h)
print_nodes(res)