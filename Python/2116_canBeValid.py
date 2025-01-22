class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        1. 定義 valid parenthesis，一個 '(' 必定和一個 ')' 相配
        且具有先後順序，像是 '()' 或 '(())'，但是 '()))' 就是錯的
        2. 算法會透過一個 stack 來統計 '(' 的數量，若拿到 ')' 時
        stack 為空，則代表 invalid
        3. 若該位置 locked[i] 為 0，則可以有機會將 ')' 改為 '('，
        並將 '(' 放入 stack
        """
        num_of_open_parenthesis = 0
        for idx, char in enumerate(s):
            if char == "(":
                num_of_open_parenthesis += 1
            else:
                # 若 locked[idx] == 1，則不可以改變括號方向
                if locked[idx] == 1:
                    if num_of_open_parenthesis == 0:
                        return False
                    else:
                        num_of_open_parenthesis -= 1
                else:
                    if num_of_open_parenthesis == 0:
                        num_of_open_parenthesis += 1
                    else:
                        num_of_open_parenthesis -= 1
        return True if num_of_open_parenthesis == 0 else False
        
# Example 1.
# Input: s = "))()))", locked = "010100"
# Output: true
res = Solution().canBeValid(s = "))()))", locked = "010100")
print(res)

# Example 2:
# Input: s = "()()", locked = "0000"
# Output: true
res = Solution().canBeValid(s = "()()", locked = "0000")
print(res)

# Example 3:
# Input: s = ")", locked = "0"
# Output: false
res = Solution().canBeValid(s = ")", locked = "0")
print(res)