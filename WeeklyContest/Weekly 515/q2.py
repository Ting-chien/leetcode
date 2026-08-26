class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        """
        Intuition: Find first lights[i] which is > r to get minimum penalty by Binary Search
        """

        # Sort lights
        lights.sort()

        penalty = 0
        for t in arrivalTime:
            r = t % period
            left, right = 0, len(lights) - 1
            # Find if lights[i] > r
            while left <= right:
                mid = (left + right) // 2
                if lights[mid] > r:
                    right = mid - 1
                else:
                    left = mid + 1
            # Find lights[left] > r
            if left >= len(lights):
                penalty = max(penalty, (period - r))

        return penalty