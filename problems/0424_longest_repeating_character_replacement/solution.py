from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Use a dict to store the appearance of characters
        in sliding window. Whenever the length of sliding
        window is larger than the dict, means dupicate char
        exist and need to shrink the window.
        """

        counter = defaultdict(int)
        slow, fast = 0, 0
        max_len = 0
        max_cnt = 0

        while fast < len(s):

            # Update counter
            counter[s[fast]] += 1
            max_cnt = max(max_cnt, counter[s[fast]])

            # Shrink window if appearance of different characters
            # is larger than k
            while (fast - slow + 1) - max_cnt > k:
                counter[s[slow]] -= 1
                slow += 1

            max_len = max(max_len, fast - slow + 1)

            fast += 1

        return max_len