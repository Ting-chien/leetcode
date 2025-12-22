from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = []
        

    def add(self, point: List[int]) -> None:
        """
        Add new point to points on grid.
        """
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        """
        Count number of ways to form an valid axis-aligned square. By
        valid, it means area > 0.
        """
        # Find points which is aligned to point in x direction
        x_aligned_points = [p for p in self.points if p[0] == point[0]]
        # Find points which is aligned to point in y direction
        y_aligned_points = [p for p in self.points if p[1] == point[1]]

        # Find points where its y direction in x_aligned_points
        valid_y_val = [p[1] for p in x_aligned_points]
        valid_x_val = [p[0] for p in y_aligned_points]
        # print(f"valid_x_val={valid_x_val}")
        # print(f"valid_y_val={valid_y_val}")

        cnt = 0
        for x, y in self.points:
            num_of_valid_x = len([_x for _x in valid_x_val if x == _x])
            num_of_valid_y = len([_y for _y in valid_y_val if y == _y])
            if (num_of_valid_x > 0 and x != point[0]) \
                and (num_of_valid_y > 0 and y != point[1]):
                cnt += max(num_of_valid_x, num_of_valid_y)
        
        return cnt
    

class DetectSquares:

    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for (x2, y2), c in self.cnt.items():
            if abs(x2 - x) == abs(y2 - y) and x2 != x and y2 != y:
                res += (
                    c *
                    self.cnt[(x, y2)] *
                    self.cnt[(x2, y)]
                )
        return res


# Example 1,
# Input
#  - ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
#  - [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output: [null, null, null, null, 1, 0, null, 2]
obj = DetectSquares()
print(obj.add([3,10]))
print(obj.add([11,2]))
print(obj.add([3,2]))
print(obj.count([11,10]))
print(obj.count([14,8]))
print(obj.add([11,2]))
print(obj.count([11,10]))