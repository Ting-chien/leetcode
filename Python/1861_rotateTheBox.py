from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        透過兩指針來調整當前物體的位置，最後再將矩陣翻轉
         - A stone '#'
         - A stationary obstacle '*'
         - Empty '.'
        """
        for row in box:
            left, right = 0, 0
            while right < len(row):
                # 若遇到石頭，右指針前進一格
                if row[right] == "#":
                    right += 1
                # 若遇到空格，右指針將當前位置變為石頭並向前一格
                # 左指針將當前位置變為空格並向前一格
                elif row[right] == ".":
                    row[right] = "#"
                    right += 1
                    row[left] = "."
                    left += 1
                # 若遇到障礙物，則右指針向前一格，左指針回到右指針的相同位置
                else:
                    right += 1
                    left = right
        # 最後再將 box 以順時鐘的方向旋轉
        rotated_box = [[""] * len(box) for _ in range(len(box[0]))]
        for row in range(len(box)):
            for col in range(len(box[row])):
                rotated_box[col][-1-row] = box[row][col]
        return rotated_box
    

# Example 1:
# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
res = Solution().rotateTheBox(box=[["#",".","#"]])
print(res)

# Example 2:
# Input: box = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
res = Solution().rotateTheBox(box=[["#",".","*","."],["#","#","*","."]])
print(res)

# Example 3:
# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
res = Solution().rotateTheBox(box=[["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]])
print(res)