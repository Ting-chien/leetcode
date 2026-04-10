from typing import List
from functools import reduce


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        print(f"expression={expression}")
        n = len(expression)
        def b_and(arr: List[bool]):
            ans = arr[0]
            for ele in arr:
                ans &= ele
            return ans
        def b_or(arr: List[bool]):
            ans = arr[0]
            for ele in arr:
                ans |= ele
            return ans
        def b_not(ele: bool):
            return not ele
        path = []
        for i in range(n):
            exp = expression[i]
            # print(f"exp={exp}")
            print(f"path={path}")
            if exp in [",", "(", ")"]:
                continue
            if exp in ["t", "f"]:
                path.append(True if exp == "t" else False)
            if exp == "&":
                path += [b_and(self.parseBoolExpr(expression[i+2:n-1]))]
            if exp == "|":
                res = b_or(self.parseBoolExpr(expression[i+2:n-1]))
                print(f"res={res}")
                print(f"path={path}")
                path += [res]
            if exp == "!":
                path += [b_not(self.parseBoolExpr(expression[i+2:n-1]))]
        return path
    

# Example 1:
# Input: expression = "&(|(f))"
# Output: false
# res = Solution().parseBoolExpr(expression="&(|(f))")
# print(res)

# Example 2:
# Input: expression = "|(f,f,f,t)"
# Output: true
res = Solution().parseBoolExpr(expression="|(f,f,f,t)")
print(res)

# Example 3:
# Input: expression = "!(&(f,t))"
# Output: true
# res = Solution().parseBoolExpr(expression="!(&(f,t))")
# print(res)

# def b_and(arr: List[bool]):
#     ans = arr[0]
#     for ele in arr:
#         ans &= ele
#     return ans
# def b_or(arr: List[bool]):
#     ans = arr[0]
#     for ele in arr:
#         ans |= ele
#     return ans
# def b_not(ele: bool):
#     return not ele

# t1 = [True, True, False]
# t2 = [True, True, True]
# t3 = [False, False, False]
# print(b_and(t1))
# print(b_or(t1))