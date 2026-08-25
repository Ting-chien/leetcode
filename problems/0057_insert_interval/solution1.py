from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Get new start and end value
        new_s, new_e = newInterval[0], newInterval[1]

        # Find intervals on the left side of new interval
        res = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < new_s:
            res.append(intervals[idx])
            idx += 1

        # Find overlap intervals
        while idx < len(intervals) and intervals[idx][0] <= new_e:
            new_s = min(new_s, intervals[idx][0])
            new_e = max(new_e, intervals[idx][1])
            idx += 1
        res.append([new_s, new_e])

        # Append remain intervals
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1

        return res


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])) # [[1,5],[6,9]]

    # Test cases 2
    print(solution.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])) # [[1,2],[3,10],[12,16]]

    # Test cases 3
    print(solution.insert(intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7])) # [[1,2],[3,5],[6,7],[9,10]]