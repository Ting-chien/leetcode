from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node=>{self.val}"
    
def print_linked_list(head: ListNode):
    while head:
        print(head.val, end="")
        head = head.next
        if head: print("=>", end="")
    print("")

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # First condition
        if not head: return None

        # Second condition
        if head and not head.next: return head

        # If the condition didn't match the first and second statement,
        # swap the nodes
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next
    

if __name__ == '__main__':

    sol = Solution()

    # Test case 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print_linked_list(sol.swapPairs(head))

    # Test case 2
    print_linked_list(sol.swapPairs(None))

    # Test case 1
    head = ListNode(1)
    print_linked_list(sol.swapPairs(head))
