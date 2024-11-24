from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # 計算 matrix 的絕對值總和
        abs_sum = sum(sum(abs(element) for element in row) for row in matrix)
        # 檢查 matrix 中的個數，若負數的數字出現次數為偶數，則直接返回絕對值總和
        negative_number_cnt = 0
        for row in matrix:
            for element in row:
                if element < 0:
                    negative_number_cnt += 1
        if negative_number_cnt % 2 == 0:
            return abs_sum
        # 若為基數，則返回絕對值總和 - 2 * 最小的數字 
        else:
            min_abs_val = min(abs(element) for row in matrix for element in row)
            return abs_sum - 2*min_abs_val