import heapq
from tracemalloc import stop
from typing import List
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Make a graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # cost[node][flight_times] = spend_money
        cost = [[float('inf')] * (k+2) for _ in range(n)]
        cost[src][0] = 0

        # min heap = (spend_money, node, flight_times)
        hq = [(0, src, 0)]

        while hq:

            amount, node, stops = heapq.heappop(hq)

            # 如果抵達終點，返回
            if node == dst:
                return amount

            # 如果超過可停次數
            if stops > k:
                continue

            # 如果當前抵達 node 的路徑的花費比已知抵達 node 的最小花費還多
            if amount > cost[node][stops]:
                continue

            # 飛往所有和 node 相連的城市
            for nei, money in graph.get(node, []):
                new_amount = amount + money
                new_stops = stops + 1
                print(f"new_stops={new_stops}")
                # 若接著從 node 飛往 nei 時所花的金額小於當前從 src 飛往 nei 的金額
                if new_amount < cost[nei][new_stops]:
                    cost[nei][new_stops] = new_amount
                    heapq.heappush(hq, (new_amount, nei, new_stops))

        return -1


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3, k=1))  # 700

    # Test cases 2
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))  # 200

    # Test cases 3
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))  # 500
