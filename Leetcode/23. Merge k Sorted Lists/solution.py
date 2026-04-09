import heapq
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

def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def find_min_node(lists: List[Optional[ListNode]]) -> ListNode:
            """Get minimum node in this round"""
            min_idx = -1
            min_val = float("inf")
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_idx = i
                    min_val = lists[i].val
            if min_idx == -1:
                return None
            chosen = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            return chosen

        dummy = ListNode(0)
        curr = dummy
        while (node := find_min_node(lists)):
            print(f"node: {node.val}")
            print(f"curr: {curr.val}")
            curr.next = node
            curr = curr.next

        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Create a min heap to store minimum nodes from each list
        min_h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_h, (node.val, i, node))

        # Iterate through all nodes and find minimum from heap
        dummy = ListNode(0)
        curr = dummy
        while min_h:
            # Append minimum node
            val, i, node = heapq.heappop(min_h)
            curr.next = node
            curr = curr.next
            # Push next node of list to heap
            if (nxt := node.next):
                heapq.heappush(min_h, (nxt.val, i, nxt))

        return dummy.next


# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
lists = [create_list([1,4,5]), create_list([1,3,4]), create_list([2,6])]
print_list(Solution().mergeKLists(lists))

# Example 2:
Input: lists = []
Output: []
lists = []
print_list(Solution().mergeKLists(lists))

# Example 3:
# Input: lists = [[]]
# Output: []
lists = [create_list([])]
print_list(Solution().mergeKLists(lists))