from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Approach 1. Brutal Force

        For loop queries by queries[i]
            For loop intervals and check if queries[i] between intervals[j][0] and intervals[j][1]
                If valid, count interval and update min value
            Add min value to result list

        Complexity (TLE)
        * Time: O(m*n), m is len(intervals) and n is len(queries)
        * Space: O(n)
        """
        res = []
        for q in queries:
            min_val = float('inf')
            for interval in intervals:
                if interval[0] <= q and q <= interval[1]:
                    min_val = min(min_val, interval[1] - interval[0] + 1)
            res.append(min_val if min_val != float('inf') else -1)
        return res
    
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Optimize: 
        1. Sort the intervals by their size first
        2. Once the queries[i] is in sorted intervals[j], we can stop comapring

        Complexity
        * Time: O(mlogm) + O(m*n) => Actually the complexity will not O(m*n), since
        we will pruned earlier
        """
        # Sort intervals by size in ascending order
        sorted_intervals = sorted(intervals, key=lambda x: x[1] - x[0])

        # Find valid situation in sorted intervals,
        # and stop once find it.
        res = []
        for q in queries:
            size = -1
            for lower, upper in sorted_intervals:
                if lower <= q and q <= upper:
                    size = upper - lower + 1
                    break
            res.append(size)
            
        return res

import heapq
from collections import deque

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # Sort intervals by left-side value
        sort_intervals = deque(sorted(intervals, key=lambda x: x[0]))
        # Sort queries by value (index should be store in the same time)
        sort_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])

        res = [-1] * len(queries)
        min_h = []
        # For loop query and index in sort_queries, and check if interval is valid
        for query, idx in sort_queries:

            # Every time, we find valid (query >= left-side) interval and push to heap
            while sort_intervals and query >= sort_intervals[0][0]:
                left, right = sort_intervals.popleft()
                heapq.heappush(min_h, (right-left+1, right))

            # Then, check if right-side >= query, pop out interval if not
            while min_h and min_h[0][1] < query:
                heapq.heappop(min_h)

            # Get the smallest interval in heap, if heap empty return -1
            res[idx] = min_h[0][0] if min_h else -1

        # Return result by index order
        return res
    

# Example 1:
# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]
res = Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])
print(res)

# Example 2:
# Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# Output: [2,-1,4,6]
res = Solution().minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22])
print(res)