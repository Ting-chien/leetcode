class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        """
        Intuition: Abstract max digits n times to find largest answer.

        Approach:
        1. Check if s is valid or 0
        2. Abstract s from 9 to 0 n times
        3. Return -1 if s is invalid
        4. Go to next loop if s is valid
        5. Assemble digits in res
        """

        # Check if s is valid or 0
        if s > 9*n:
            return -1

        if s == 0:
            return 0

        # Try n times
        res = []
        for i in range(n):
            for digit in range(9, -1, -1):
                s -= digit
                if s > 9*(n - i - 1):
                    return -1
                if s >= 0:
                    res.append(digit)
                    break
                if s < 0:
                    s += digit
                    continue

        return int("".join([str(r) for r in res]))


print(Solution().largestInteger(n=2, s=9)) # 90
print(Solution().largestInteger(n=2, s=19)) # -1
print(Solution().largestInteger(n=5, s=0)) # 0