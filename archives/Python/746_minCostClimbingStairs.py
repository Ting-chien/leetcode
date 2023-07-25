from operator import le
from typing import List

class Solution1:
    '''DP(Top-down)'''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.dp(len(cost)-1, cost, [None]*len(cost)), self.dp(len(cost)-2, cost, [None]*len(cost)))

    def dp(self, n, cost, result):
        if n == 0 or n == 1:
            return cost[n]
        if not result[n]:
            result[n] = min(self.dp(n-1, cost, result), self.dp(n-2, cost, result)) + cost[n]
        return result[n]

class Solution2:
    '''DP(Bottom-up)'''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [None]*(len(cost))
        result[0], result[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            result[i] = min(result[i-1], result[i-2]) + cost[i]
        print(result)
        return min(result[-1], result[-2])

class Solution3:
    '''DP(Bottom-up) with lower memory usage'''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)

if __name__ == '__main__':
    sol = Solution3()
    print(sol.minCostClimbingStairs([10,15,20]))
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))