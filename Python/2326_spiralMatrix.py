from typing import Optional, List
from utils.linked_list import insert_nodes, print_nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """
        1. 先建立一個值都會 -1 的 mn 矩陣
        2. 依照 [[0, 1], [1, 0], [0, -1], [-1, 0]] 的順序走下去
        3. 若遇到邊界 i >= m or i < 0 or j >= n or j < 0 or mn[i][j] != -1 則換方向
        """
        i, j, step = 0, 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        mn = [[-1 for _ in range(n)] for _ in range(m)]

        # Go through nodes in linked-list
        while head:
            if (i >= m
                or i < 0
                or j >= n
                or j < 0
                or mn[i][j] != -1):
                i += directions[step][0]
                j += directions[step][1]