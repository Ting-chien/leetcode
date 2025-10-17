class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Approach: DP

        Complexity
         - Time: O(n^2)
         - Space: O(n^2)
        """
        n = len(s)
        # 用一個二維陣列，dp[i][j] 表示字串 s[i:j+1] 為有效字串
        dp = [[False]*n for _ in range(n)]

        # 先把單一個字時為 "*" 的情況設為 True
        for i in range(n):
            if s[i][i] == "*":
                dp[i][i] = True

        # 接著檢查長度為 2 以上的子字串
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                # 直接檢查 s[i:j+1] 是否有效，若頭尾已經
                # 確認為有效，那只要檢查中間是否還有字符，或
                # 從 i+1~j-1 是否有錢
                if i in "(*" and j in "*)":
                    if length == 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                # 如無效，檢查把 s[i:j+1] 拆為兩段是否有效
                # 譬如 s=()()
                if not dp[i][j]:
                    for k in range(i, j):
                        # if dp[i][k] and dp[k][j]:
                        if dp[i][k] and dp[k+1][j]:
                            dp[i][j] = True

        # return dp[0][n]
        return dp[0][n-1]
    

class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Approach: Greedy

        Complexity
         - Time: O(n)
         - Space: O(1)
        """
        # 使用 min_open, max_open 來紀錄最少和最多可能
        # 存在的尚未配對左括號
        min_open = 0
        max_open = 0

        for char in s:
            if char == "(":
                min_open += 1
                max_open += 1
            elif char == ")":
                max_open -= 1
                min_open -= 1
            elif char == "*":
                # '*'當作'('
                # min_open += 1 ❌
                max_open += 1
                # '*'當作')'
                # max_open -= 1 ❌
                min_open -= 1

            # 假設 max_open < 0 代表優先出先了一個右括號
            # 整個字串必定為無效
            if max_open < 0:
                return False
            
            # min_open 也不可小魚 0 因為不可預設配對
            min_open = max(min_open, 0)

        return min_open == 0