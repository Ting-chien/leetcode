from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        這題和 435. Non-overlapping Intervals 很類似，差別在於 435 是要
        提除重疊的區間並返回剔除的次數，而 452 是要計算總共有多少未重疊的區間，
        其他重疊的區間就不用管他了，因為一定會在範圍內被箭設中。

        Complexity
        * Time: O(nlogn) - beats 89.66%
        * Space: O(1) - beats 34.33%
        """
        points.sort(key=lambda x: x[1])
        cnt, global_end = 0, float("-inf")
        for start, end in points:
            if start >= global_end:
                global_end = end
                cnt += 1
        return cnt