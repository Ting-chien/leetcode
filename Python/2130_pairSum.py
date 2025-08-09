from typing import Optional
from utils.linked_list import insert_nodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Use an array to store all nodes' value, and add 
        each value of arr[:n/2-1] to arr[n/2:]

        1. Go throught linked list and store values in arr
        2. Split arr into first and second half
        3. Iterate through both array and find max

        Complexity
        * Time: O(n) - beats 70.53%
        * Space: O(n) - beats 10.56%
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)
        max_val = 0
        for v1, v2 in zip(arr[:n//2], arr[n//2:][::-1]):
            max_val = max(max_val, v1+v2)

        return max_val
    

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
head = insert_nodes([5,4,2,1])
res = Solution().pairSum(head)
print(res)

# Example 2:
# Input: head = [1,100000]
# Output: 100001
head = insert_nodes([1,100000])
res = Solution().pairSum(head)
print(res)
