from typing import List, Optional


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