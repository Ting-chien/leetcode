class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        """
        Approach: 
        1. Get max timestamp from last element of s1 and s2
        2. Turn s1 and s2 to map
        3. 
        """

        max_t = max(series1[-1][0], series2[-1][0])

        p1, p2 = len(series1)-1, len(series2)-1 # Use two pointers to track timestamp in both series
        v1, v2 = 0, 0 # Use two variables to record current series value
        t1, t2 = series1[-1][0], series2[-1][0] # Store current timestamp

        res = []
        for t in range(max_t, 0, -1):
            print(f"t={t}")

            # Find timestamp t in s1
            while p1 >= 0 and t <= series1[p1][0]:
                v1 = series1[p1][1]
                t1 = series1[p1][0]
                p1 -= 1

            # Find timestamp t in s2
            while p2 >= 0 and t <= series2[p2][0]:
                v2 = series2[p2][1]
                t2 = series2[p2][0]
                p2 -= 1

            print(f"p1={p1}, p2={p2}")
            print(f"t1={t1}, t2={t2}")
            # Skip if both series have no value
            if t1 > t and t2 > t:
                continue

            res.append([t, v1+v2])

        # print(res)
        return res


if __name__ == "__main__":

    # Example 1:
    series1 = [[1,3],[4,1]]
    series2 = [[2,2],[5,2]]
    print(Solution().aggregateTimeSeries(series1, series2)) # [[1,5],[2,3],[4,3],[5,2]]

    # Example 2:
    series1 = [[1,5],[3,1]]
    series2 = [[2,2]]
    print(Solution().aggregateTimeSeries(series1, series2)) # [[1,7],[2,3],[3,1]]

    # Example 3:
    series1 = [[1,5]]
    series2 = [[1000000000,2]]
    print(Solution().aggregateTimeSeries(series1, series2)) # [[1,7],[1000000000,2]]