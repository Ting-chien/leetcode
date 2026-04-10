from typing import List, Tuple
from sympy import simplify, symbols


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Get a list of equations with division of two arguments, return the query of those variables.

        e,g,.

            equations=[["a","b"], ["b","c"]], values=[2.0, 3.0]

            1. Can I find each value of a, b, and c ? => No

            So, we have to use equaiton results to calculate value for queries.

            => How ? Use `sympy` to check to equation expression are identical.

        """

        # Get all combination of equations
        N = len(equations)
        expressions = {} # Store (dividend, divisor)
        def dfs(start: int, exp: Tuple[Tuple[str], Tuple[str]], val: float):
            # Store expression and result to expressions
            expressions[exp] = val
            # Get all combinations
            for i in range(start, N):
                dfs(i+1, (exp[0]+(equations[i][0]), exp[1]+(equations[i][1])), val+values[i])
        dfs(0, ((), ()), 0)

        print(expressions)

        # 整理 expressions
        # for dividend, divisor

        # # Get all results in queries
        # ans = []
        # for q in queries:
        #     exp = simplify(q)
        #     if exp in expressions:
        #         ans.append(expressions[exp])
        #     else:
        #         ans.append(-1)

        # return ans
    

# Example 1:
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
res = Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
print(res)