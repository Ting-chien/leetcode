from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort(key=lambda x: x[0])

        res = 0
        for r in robot:
            for f in factory:
                if f[1] > 0:
                    f[1] -= 1
                    res += abs(f[0]-r)
                    break

        return res     


# Example 1
# Input: robot = [0,4,6], factory = [[2,2],[6,2]]
# Output: 4
res = Solution().minimumTotalDistance([0,4,6], [[2,2],[6,2]])
print(res)

# Example 2
# Input: robot = [1,-1], factory = [[-2,1],[2,1]]
# Output: 2
res = Solution().minimumTotalDistance([1,-1], [[2,1],[-2,1]])
print(res)