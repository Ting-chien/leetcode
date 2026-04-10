from typing import List
from datetime import datetime


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        1. 先跑過一次 sort() 讓 timePoints 根據我們要的大小排列
        2. 在跑過一次 timePoints 所有的時間，並計算時間差
        """

        # 取得排列好的時間搓序列
        sorted_time_points = sorted(timePoints)
        print(sorted_time_points)
        # 將該時間搓由小到大逐一遍歷，並同時比較時間差
        min_diff = float("inf")
        for i in range(len(sorted_time_points)):
            dt1 = datetime.strptime(sorted_time_points[i], "%H:%M")
            dt2 = datetime.strptime(sorted_time_points[0 if i == len(sorted_time_points)-1 else i+1], "%H:%M")
            diff = (dt2-dt1).seconds
            min_diff = min(min_diff, diff/60 if diff else diff)
        return int(min_diff)
    

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        1. Convert input into minutes and sort times in ascending order
        2. Find minimun difference between each adjacent time
        """
        # convert input to minutes
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        # sort times in ascending order
        minutes.sort()
        # find minimum difference across adjacent elements
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
        # consider difference between last and first element
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])


if __name__ == "__main__":

    # # Example 1:
    # # Input: timePoints = ["23:59","00:00"]
    # # Output: 1
    # res = Solution().findMinDifference(timePoints=["23:59","00:00"])
    # print(res)

    # # Example 2:
    # # Input: timePoints = ["00:00","23:59","00:00"]
    # # Output: 0
    # res = Solution().findMinDifference(timePoints=["00:00","23:59","00:00"])
    # print(res)

    # Example 3:
    # Input: timePoints = ["05:31","22:08","00:35"]
    # Output: 147
    res = Solution().findMinDifference(timePoints=["05:31","22:08","00:35"])
    print(res)