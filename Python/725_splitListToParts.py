from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''Solution 1. Split the nodes seperately if the numbers of 
    nodes is smaller than k, or save the node in value of len(nodes)/k
    '''
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # Count the len of list
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # Divide the count by k
        res = []
        q, mod = divmod(count, k)
        for _ in range(k):
            curr = head
            steps = q+1 if mod > 0 else q
            while steps > 1:
                curr = curr.next
                steps -= 1
            if head:
                res.append(head)
                head = curr.next
                curr.next = None
                mod -= 1
            else:
                res.append(None)
        # if count // k > 0:
        #     # Save the nodes by size of quitient
        # else:
        #     # Size = 1
        return res
        

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node10 = ListNode(10)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    sol = Solution()
    res_list = sol.splitListToParts(node1, 3)
    for res in res_list:
        while res != None:
            if res.next == None:
                print(res.val)
            else:
                print(res.val, "->", end=" ")
            res = res.next