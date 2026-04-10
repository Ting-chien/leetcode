from typing import List, Optional

from utils.linked_list import print_nodes, insert_nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Iterate through the linked list from head
        2. Check if the node value exist in nums
        """
        # Tranform nums from list to hash map for efficiency issue
        nums = set(nums)

        prev, curr = None, head
        while curr:
            # Check if node value exist in nums,
            # and remove the node if value exist.
            if curr.val in nums:
                if prev:
                    # Check if prev exist, remove current
                    # node if exist.
                    prev.next = curr.next
                else:
                    # Remove current node and replace head
                    # with next node if not exist.
                    head = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return head
    

if __name__ == "__main__":

    # Example 1
    # Input: nums = [1,2,3], head = [1,2,3,4,5]
    # Output: [4,5]
    head = insert_nodes([1,2,3,4,5])
    print_nodes(Solution().modifiedList(nums=[1,2,3], head=head))

    # Example 2
    # Input: nums = [1], head = [1,2,1,2,1,2]
    # Output: [2,2,2]
    head = insert_nodes([1,2,1,2,1,2])
    print_nodes(Solution().modifiedList(nums=[1], head=head))

    # Example 3
    # Input: nums = [5], head = [1,2,3,4]
    # Output: [1,2,3,4]
    head = insert_nodes([1,2,3,4])
    print_nodes(Solution().modifiedList(nums=[5], head=head))