from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solve this question by Set data structure.

        First, remove duplicate number in nums - O(n)

        Sencond, iterate through the set, and find if x is the first number in the group.
        If the first number, find out the size of the group by adding `1` to the
        number each time. If not, skip. - O(n)

        For example, s = {1, 3, 4} => 1, 3 are first number in their group

        """

        # Turn list into set
        s = set(nums)

        # Iterate through set
        max_len = 0
        for num in s:
            # Count length of LCS only start from the first element
            if (num - 1) not in s:
                curr_len = 1
                curr_num = num
                while (curr_num + 1) in s:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)

        return max_len