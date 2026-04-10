from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Use a variable max_alt to store highest altitude.
        """
        curr = max_alt = 0
        for alt in gain:
            curr += alt
            max_alt = max(max_alt, curr)
        return max_alt