class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        """
        Intuition: Iterate through drones and compare with the smallest 
        Manhattan distance and index
        """
        min_dis = float('inf')
        ans = -1
        tx, ty = target[0], target[1]
        for idx, val in enumerate(drones):
            dx, dy, range = val[0], val[1], val[2]
            distance = (abs(tx - dx) + abs(ty - dy))
            if (distance <= range):
                if distance < min_dis:
                    min_dis = distance
                    ans = idx
        return ans