import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        Use a heap with length candidates*2 to store first and last workers
        cost. Get the smallest one and push a new worker to heap.

        Results: Failed ❌ (Spend 49:14)
        """
        N = len(costs)
        heap = []
        for i in range(candidates):
            heap.append((costs[i], i))
        for i in range(N-1, N-candidates, -1):
            heap.append((costs[i], i))
        heapq.heapify(heap)
        left, right = candidates, N-candidates-1

        total = 0
        for i in range(k):
            print(f"left={left}, right={right}")
            # 取出最小的 cost worker
            cost, idx = heapq.heappop(heap)
            total += cost
            # 判斷要插入左側還右側的 costs
            if idx > right:
                if right > 0:
                    heapq.heappush(heap, (costs[right], right))
                    right -= 1
            else:
                if left < len(costs)-1:
                    heapq.heappush(heap, (costs[left], left))
                    left += 1

        return total
    

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        如果一個 heap 不行，那就用兩個啊！（餐考 ChatGPT）
        """
        N = len(costs)
        left_h, right_h = [], []
        
        # 初始化 left_h, right_h
        left, right = 0, N-1
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_h, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_h, (costs[right], right))
                right -= 1

        # 選 k 次
        total = 0
        for _ in range(k):
            left_worker = heapq.heappop(left_h) if left_h else None
            right_worker = heapq.heappop(right_h) if right_h else None
            if left_worker and right_worker:
                if left_worker[0] <= right_worker[0]:
                    # 左邊比較小，用左邊的
                    total += left_worker[0]
                    if left <= right:
                        heapq.heappush(left_h, (costs[left], left))
                        left += 1
                    # 補回去右邊的
                    heapq.heappush(right_h, (right_worker[0], right_worker[1]))
                else:
                    # 右邊比較小，用右邊的
                    total += right_worker[0]
                    if left <= right:
                        heapq.heappush(right_h, (costs[right], right))
                        right -= 1
                    # 補回去左邊的
                    heapq.heappush(left_h, (left_worker[0], left_worker[1]))
            elif left_worker:
                total += left_worker[0]
                if left <= right:
                    heapq.heappush(left_h, (costs[left], left))
                    left += 1
            elif right_worker:
                total += right_worker[0]
                if left <=right:
                    heapq.heappush(right_h, (costs[right], right))
                    right -= 1
            else:
                break
        
        return total
    

# Example 1:
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
res = Solution().totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)
print(res)

# Example 2:
# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
res = Solution().totalCost(costs = [1,2,4,1], k = 3, candidates = 3)
print(res)

# heap=[(1,0), (1, 3), (2, 1), (4, 2)], left=3, right=0

# total=1, idx=0==right => push left