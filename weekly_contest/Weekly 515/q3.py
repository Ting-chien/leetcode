class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        """
        Intuition: Use Greedy to get to array. One is the worker
        assigned to the most left side of station. The other
        array is the workers assigned to the most right side of 
        station. The answer will be the 

            ans = max(right[i+1] - left[i] for 0 .. n-1)

        Complexity
        - Time: O(n+m)
        - Space: O(2n)
        """
        n, m = len(skill), len(station)

        # If only one worker, the gap is 0
        if n == 0:
            return 0

        # Find the earliest possible station index for workers
        left = [0] * n
        j = 0
        for i in range(n):
            while station[j] != skill[i]:
                j += 1
            left[i] = j
            j += 1

        # Find the latest possible station index for workers
        right = [0] * n
        j = m - 1
        for i in range(n-1, -1, -1):
            while station[j] != skill[i]:
                j -= 1
            right[i] = j
            j -= 1

        # Matching j_i and j as far as possible by two arrays
        ans = 0
        for i in range(n - 1):
            ans = max(ans, (right[i+1] - left[i]))

        return ans