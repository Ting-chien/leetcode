from typing import List, Optional, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_nodes(arr: List[Any]) -> Optional[ListNode]:
    dummy = curr = ListNode(0)
    for ele in arr:
        curr.next = ListNode(ele)
        curr = curr.next
    return dummy.next

def print_nodes(node: Optional[ListNode]) -> List[Any]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)
    return res

