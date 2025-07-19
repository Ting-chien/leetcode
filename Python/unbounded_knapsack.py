from typing import List
from functools import cache


def unbounded_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    @cache
    def dfs(i: int, cap: int):
        """
        :param i: Number of items to be select
        :param cap: Left capacity of backpack
        """
        # no item to choose
        if i < 0:
            return 0
        # no capacity 
        if wgt[i] > cap:
            return dfs(i-1, cap)
        # decide to select or not
        return max(dfs(i-1, cap), dfs(i, cap-wgt[i])+val[i])
    return dfs(len(wgt)-1, capacity)

def unbounded_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    """
    直接使用動態規劃(DP)，和0-1背包問題的差別在於物品可以複選，所以選或不選的問題變成
    
        選：與0-1背包问题不同，轉移至 [i, c-wgt[i-1]]
        不選：與0-1背包問題相同，轉移至 [i-1, c]
    """
    N = len(wgt)
    dp = [[0] * (capacity+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for c in range(1, capacity+1):
            # No choose
            if wgt[i-1] > c:
                dp[i][c] = dp[i-1][c]
            else:
            # Choose or not choose
                dp[i][c] = max(dp[i][c-wgt[i-1]]+val[i-1], dp[i-1][c])
    return dp[N][capacity]

res = unbounded_knapsack(capacity=50, wgt=[10,20,30,40,50], val=[50,120,150,210,240])
print(res)