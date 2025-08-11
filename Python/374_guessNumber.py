# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

pick = 0
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Use binary search to find the number you pick,
        if the number I guess > your pick (-1), right = middle
        if the number I guess < your pick (1), left = middle
        if the number I guess = your pick (0), return number

        Edge cases:
         - Pick [1, n]

        Complexity:
         * Time O(logn) - beats 86.32%
         * Space O(1) - beats 27.87%

        Spend: 11:09
        """
        left, right = 1, n
        while left <= right:
            middle = (left+right) // 2
            if guess(middle) == -1:
                right = middle - 1
            elif guess(middle) == 1:
                left = middle + 1
            else:
                return middle