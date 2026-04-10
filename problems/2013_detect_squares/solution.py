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
        # Appearance of each coordinates
        self.counter = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.counter[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        # Iterate all points on grid, check
        # 1. Whether the edges along x and y direction are equal
        # 2. Two points are not the same
        x1, y1 = point[0], point[1]

        cnt = 0
        for x2, y2 in self.counter.keys():
            if abs(x1 - x2) == abs(y1 - y2) and x1 != x2 and y1 != y2:
                # Count the product of the appearance of three corners
                cnt += self.counter[(x2, y2)] \
                    * self.counter[(x1, y2)] \
                    * self.counter[(x2, y1)]
                
        return cnt


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