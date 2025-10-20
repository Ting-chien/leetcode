from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        res = []
        def backtrack(remain: int, open: int = 0, path: str = ""):
            """
            :param remain: Number of parentheses need to be put in the path.
            :param open: Number of open parentheses in the path.
            :param path: Permutation of n parentheses.
            """
            # return when all parentheses are used
            if remain == 0:
                res.append(path)
                return
            # 當左括號數量還不到總數的一半時，可以繼續放入左括號
            if open < n:
                backtrack(remain-1, open+1, path+"(")
            # 當現在 path 中的左括號比右括號多時，可以放入右括號
            if 2*n-remain-open < open:
                backtrack(remain-1, open, path+")")

        backtrack(2*n)
        return res
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Algorithm: Backtracking

        Complexity
         - Time: O(2^n) - beats 100%
         - Space: O(n) - beats 69.93%
        """
        expressions = [] # All expressions in result
        
        def dfs(open: int, close: int, expr: str):
            """
            Args:
                open: Number of open bracket
                close: Number of close bracket
                expr: Current expression 
            """
            # Base case
            if len(expr) == 2*n:
                expressions.append(expr)
            # General case
            for bracket in ("(", ")"):
                if bracket == "(":
                    if open < n and open >= close:
                        dfs(open+1, close, expr+bracket)
                if bracket == ")":
                    if close < n and close < open:
                        dfs(open, close+1, expr+bracket)

        dfs(0, 0, "")
        return expressions
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 初始化一個長度為 n+1 的 dp 陣列，dp[i] 代表 n=i 時的有效排列
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        # 透過 "(" + [i對括號的有效組合] + ")" + [i-1+j對括號的有效組合]
        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        dp[i].append(f"({left}){right}")
        return dp[n]


# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
res = Solution().generateParenthesis(n=3)
print(res)

# Example 2:
# Input: n = 1
# Output: ["()"]
res = Solution().generateParenthesis(n=1)
print(res)