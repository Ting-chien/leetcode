from typing import List
from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        DFS (Time Limit Exceed)
        Time:
        Space:
        """
        # Turn flights information into a direction graph
        graph = {i: [] for i in range(n)} # [to, price]
        for start, to, price in flights:
            graph[start].append([to, price])

        # Find minumun cost recursively
        min_cost = float('inf')
        visited = set()
        def dfs(remain: int, curr: int, cost: int):
            """
            Args:
                :remain: Remain times to stop
                :curr: Current position
                :cost: Cost for traveling from src to curr
            """
            # Retunr if we arrive destination
            if curr == dst:
                nonlocal min_cost
                min_cost = min(min_cost, cost)
                return
            # Return if we ran out of stop times
            if remain < 0:
                return
            # Iterate all available paths
            for to, price in graph[curr]:
                if to not in visited:
                    visited.add(to)
                    dfs(remain-1, to, cost+price)
                    visited.remove(to)
        
        dfs(k, src, 0)
        return -1 if min_cost == float('inf') else min_cost

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for a, b, c in flights:
            graph[a].append((b, c))

        min_dis = [float('inf') for _ in range(n)]

        count = 0
        # 距離, idx
        temp = deque([(0, src)])
        while temp and count < k+1:
            for _ in range(len(temp)):
                currDis, node = temp.popleft()
                for nextNode, nextDis in graph[node]:
                    if min_dis[nextNode] > nextDis+currDis:
                        min_dis[nextNode] = nextDis+currDis
                        temp.append((nextDis+currDis, nextNode))
            count += 1
        return min_dis[dst] if min_dis[dst] != float('inf') else -1
    

# Example 2:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
res = Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)
print(res)

# Example 3:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 200
res = Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0)
print(res)