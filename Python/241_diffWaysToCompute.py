import re
from typing import List


class Solution1:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        1. 先把 expression 拆成數值 nums 和運算子 ops 兩部分
        2. 針對 nums 和 ops 做 dfs，判斷條件為
            2-1. 若 ops 有值，則繼續往下遍歷
            2-2. 若 ops 為空，則將當下的結果紀錄在 exprDict
        3. 返回 exprDict
        """
        d = {}
        nums, ops = [], []
        # Separate number and operator into nums and ops
        expression = re.split(r'(\D)', expression)
        for e in expression:
            if e.isdigit():
                nums.append(e)
            else:
                ops.append(e)
        self.dfs(nums, ops, d)
        return d.values()
    
    def dfs(self, nums: List[str], ops: List[str], d: dict):
        """
        用途：往下遍歷所有計算的組合方式，若運算子已全部用完，則紀錄
        計算結果並返回。
        """
        if ops:
            for i in range(len(ops)):
                self.dfs(
                    nums=nums[:i] + ["(" + nums[i] + ops[i] + nums[i+1] + ")"] + nums[i+2:],
                    ops=ops[:i] + ops[i+1:],
                    d=d
                )
        else:
            d[nums[0]] = eval(nums[0])


class Solution2:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        1. 遍歷整個 expression
        2. 若遇到運算子，則將左右兩側的 subexpression 往下做遞迴
        3. 當遇到只有單一個數字（或無運算子）的情況，則返回該數字
        4. 拿左右兩側的 subexpression 遞迴結果做計算，接著返回
        """
        res = []
        # Iterate through all elements
        for i in range(len(expression)):
            # Separate left and right subexpression, and 
            # calculate the different permutations on each
            # left, right and operator.
            if expression[i] in "+-*":
                l_exps = self.diffWaysToCompute(expression[:i])
                r_exps = self.diffWaysToCompute(expression[i+1:])
                for l_exp in l_exps:
                    for r_exp in r_exps:
                        ops = expression[i]
                        if ops == "+":
                            res.append(l_exp+r_exp)
                        if ops == "-":
                            res.append(l_exp-r_exp)
                        if ops == "*":
                            res.append(l_exp*r_exp)
        # Return number if there is no operator
        if not res:
            res.append(int(expression))
        return res


if __name__ == "__main__":

    # Example 1:
    # Input: expression = "2-1-1"
    # Output: [0,2]
    res = Solution2().diffWaysToCompute(expression="2-1-1")
    print(res)

    # Example 2:
    # Input: expression = "2*3-4*5"
    # Output: [-34,-14,-10,-10,10]
    res = Solution2().diffWaysToCompute(expression="2*3-4*5")
    print(res)
