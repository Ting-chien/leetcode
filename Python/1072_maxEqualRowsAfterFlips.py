from typing import List


class Solution1:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 宣告一變數用儲存擁有最多相同值得 row 的數量
        max_identical_rows = 0
        # 遍歷每一層 row 去尋找和該 row 完全相同或完全相反的 row 的數量
        for row in matrix:
            # 先找到和 row 完全相反的 row
            reverse_row = [1-x for x in row]
            # 在取找和 row 完全相同或完全相反的 row 的數量
            identical_rows = sum([1 for compare_row in matrix \
                                  if compare_row == row or compare_row == reverse_row
                                ])
            # 比較每一層的計算結果並找出最大
            max_identical_rows = max(max_identical_rows, identical_rows)
        return max_identical_rows
    
class Solution2:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 建立一個用來儲存 pattern 出現次數的 map
        pattern_cnt = {}
        # 遍歷所有的 row
        for row in matrix:
            # 將 row 轉為固定的格式，定義低一個字符一定是 T
            # 和第一個字符值相同的欄位填 T，不同的填 F
            pattern = ["T" if x == row[0] else "F" for x in row]
            # 將 pattern 轉為字串方便 map 的鍵值
            pattern_str = "".join(pattern)
            pattern_cnt[pattern_str] = pattern_cnt.get(pattern_str, 0) + 1
        return max(pattern_cnt.values())
    

# Example 1:
# Input: matrix = [[0,1],[1,1]]
# Output: 1
res = Solution2().maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]])
print(res)

# Example 2:
# Input: matrix = [[0,1],[1,0]]
# Output: 2
res = Solution2().maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]])
print(res)

# Example 3:
# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
res = Solution2().maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]])
print(res)