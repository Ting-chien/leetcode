from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        先透過 binary search 找到 target 可能存在哪一個 row，再到該 row 裡尋找
        target 的位置。

        Complexity
         - Time: O(log(m*n))
         - Space: O(1)
        """

        m, n = len(matrix), len(matrix[0])

        # Find which row might have target
        row = -1
        top, bot = 0, m-1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            else:
                row = mid
                top = mid + 1

        # Find target in row
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False