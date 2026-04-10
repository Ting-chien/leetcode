import math
from typing import List
from collections import defaultdict

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        How to define a valid square ?
        1. Value of width and length are equal
        2. Only two value exist in x and y direction

        => Wrong anserr in Example 3
        """
        points = [p1, p2, p3, p4]
        x_values = list(set([p[0] for p in points]))
        y_values = list(set([p[1] for p in points]))

        if len(x_values) == 2 and len(y_values) == 2 \
            and (abs(x_values[0] - x_values[1]) == abs(y_values[0] - y_values[1])):
            return True
        
        return False
    

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        How to define a valid square ?
        1. Find the center
        2. Equal value from center to four corners
        """
        def get_len(a: List[int], b: List[int]) -> int:
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        
        center = [(p1[0]+p2[0]+p3[0]+p4[0])/4, (p1[1]+p2[1]+p3[1]+p4[1])/4]
        distances = set()
        for p in (p1, p2, p3, p4):
            distances.add(get_len(center, p))
        
        return len(distances) == 1
    

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Actual principle to define a square
         - Equal length on 4 edges
         - Equal length on 2 diagnals
        """

        def get_distance_sqr(x1: int, y1: int, x2: int, y2: int) -> int:
            return (x1 - x2) ** 2 + (y1 - y2) ** 2
        
        # Combine every two points and store the distance of two points
        # into the counter
        counter = defaultdict(int)
        points = [p1, p2, p3, p4]
        for i in range(4):
            p1 = points[i]
            for j in range(i+1, 4):
                p2 = points[j]
                dis = get_distance_sqr(p1[0], p1[1], p2[0], p2[1])
                counter[dis] += 1

        # Check if 4 edges are equal and 2 diagonals are equals
        if len(counter) != 2:
            return False
        # Also, the points can not be duplicated (edge > 0)
        edges, diags = sorted(counter.items())[:2]
        return edges[0] > 0 and edges[1] == 4 and diags[1] == 2
    

# Example 1:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))

# Example 2:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))

# Example 3:
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
print(Solution().validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))

# Example 4:
# Input: p1 = [0,0], p2 = [5,0], p3 = [5,4], p4 = [0,4]
# Output: false
print(Solution().validSquare(p1 = [0,0], p2 = [5,0], p3 = [5,4], p4 = [0,4]))