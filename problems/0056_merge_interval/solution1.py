from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort intervals by start_i
        intervals.sort(key=lambda x: x[0])

        # Compare adjacent intervals
        res = []
        cur_s, cur_e = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            new_s, new_e = intervals[i][0], intervals[i][1]
            if cur_e >= new_s:
                # Overlapping, update interval
                cur_e = max(cur_e, new_e)
            else:
                # Store previous interval and create a new one
                res.append([cur_s, cur_e])
                cur_s, cur_e = new_s, new_e

        # Append the last interval
        res.append([cur_s, cur_e])

        return res


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]

    # Test cases 2
    print(solution.merge(intervals = [[1,4],[4,5]])) # [[1,5]]

    # Test cases 3
    print(solution.merge(intervals = [[4,7],[1,4]])) # [[1,7]]