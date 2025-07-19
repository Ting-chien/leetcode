from typing import List
from functools import cache


def zero_one_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    "Method 1: Brutal solve with DFS."
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
        return max(dfs(i-1, cap), dfs(i-1, cap-wgt[i])+val[i])
    return dfs(len(wgt)-1, capacity)

def zero_one_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    "Method 2: Use memo to store sub problems answert."
    memo = [[-1] * (capacity+1) for _ in range(len(wgt))]
    def dfs(i: int, cap: int):
        """
        :param i: Number of items to be select
        :param cap: Left capacity of backpack
        """
        # no item to choose
        if i < 0:
            return 0
        # return if the answer has been calculated
        if memo[i][cap] != -1:
            return memo[i][cap]
        # no capacity 
        if wgt[i] > cap:
            return dfs(i-1, cap)
        # decide to select or not
        max_val = max(dfs(i-1, cap), dfs(i-1, cap-wgt[i])+val[i])
        memo[i][cap] = max_val
        return max_val
    ans = dfs(len(wgt)-1, capacity)
    return ans

def zero_one_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    "Method 3: Use Python functools to optimize memorization."
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
        return max(dfs(i-1, cap), dfs(i-1, cap-wgt[i])+val[i])
    return dfs(len(wgt)-1, capacity)

def zero_one_knapsack(capacity: int, wgt: List[int], val: List[int]) -> int:
    """
    Method 4: Use DP to calculate the max value in each state.
    
        - 時間複雜度：O(n*cap)
        - 空間複雜度：O(n*cap)
    """
    # 建立一個二維DP，長寬設為len(wgt)+1和capacity+1的原因是當不選時，可以往上一個計算
    # 結果參考，而參考的基準值就是沒有物品(i=0)或沒有空間(cap=0)，此時背包的價值必為0。
    dp = [[0] * (capacity+1) for _ in range(len(wgt)+1)]
    for i in range(1, len(wgt)+1):
        for c in range(1, capacity+1):
            # 若物品重量>背包容量則不選，所以此時背包的價值和前i-1個物品的計算結果一樣
            if wgt[i-1] > c:
                dp[i][c] = dp[i-1][c]
            # 若物品重量<=背包容量，可自行選擇選或不選
            else:
                dp[i][c] = max(dp[i-1][c], dp[i-1][c-wgt[i-1]]+val[i-1])
    return dp[len(wgt)][capacity]


res = zero_one_knapsack(capacity=50, wgt=[10,20,30,40,50], val=[50,120,150,210,240])
print(res)
