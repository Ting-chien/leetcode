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