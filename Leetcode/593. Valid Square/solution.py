import math
from typing import List

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