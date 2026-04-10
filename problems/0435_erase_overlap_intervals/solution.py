from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        You will be given intervals, find minimum number of intervals
        to be remove to make non-overlapping.

        For example,

            intervals=[[1,2],[2,3],[3,4],[1,3]]

        Approach
        1. Sort intervals by first and second index of value
        2. Iterate through intervals and check if end[i] > start[j],
        if though, remove one of them

        Result: ❌
        Reason: 優先排序 start 的話有可能該 interval 的結束時間很晚，這樣
        後面再比對時要刪除的 intervals 就很多。正確的做法應該是要優先排序 end，
        並且和前一時段做比較。
        """
        # Sort interval by first and second index of value
        # Python built-in function will sort in a wise way, and
        # there is a more explicit way by sort(key=lambda x: (x[0], x[1]))
        intervals.sort()

        cnt, i, n = 0, 1, len(intervals)
        while i < n:
            end = intervals[i-1][1]
            start = intervals[i][0]
            if end > start:
                intervals.pop(i)
                cnt += 1
                n -= 1
                continue
            i += 1

        return cnt
    

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        You will be given intervals, find minimum number of intervals
        to be remove to make non-overlapping.

        For example,

            intervals=[[1,2],[2,3],[3,4],[1,3]]

        Approach
        1. Sort intervals by first and second index of value
        2. Iterate through intervals and check if end[i] > start[j],
        if though, remove one of them

        Result: ✅
        """
        intervals.sort(key=lambda x: x[1])

        cnt, i, n = 0, 1, len(intervals)
        while i < n:
            end = intervals[i-1][1]
            start = intervals[i][0]
            if end > start:
                intervals.pop(i) # 在迴圈中 pop 複雜度可能到 O(N^2)
                cnt += 1
                n -= 1
                continue
            i += 1

        return cnt
    

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        原本的解法還要去改動 intervals 裡的值效能很差，直接用一個全域變數來記住
        現在的 end，如果當下的 start > interval_end 就當作跳過。

        Complexity
        * Time: O(nlogn) - beats 37.24%
        * Space: O(1) - beats 21.67%
        """
        intervals.sort(key=lambda x: x[1])
        cnt, global_end = 0, float("-inf")
        for start, end in intervals:
            if start >= global_end:
                global_end = end
            else:
                cnt += 1
        return cnt


# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
res = Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]])
print(res)

# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
res = Solution().eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]])
print(res)

# Example 3:
# Input: intervals = [[1,2]]
# Output: 0
res = Solution().eraseOverlapIntervals(intervals = [[1,2]])
print(res)

# Example 3:
# Input: intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
# Output: 0
res = Solution().eraseOverlapIntervals(intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
print(res)