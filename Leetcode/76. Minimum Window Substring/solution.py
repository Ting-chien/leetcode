class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Intuition: Expand the window if condition not match, while
        shrink the window if condition match. Condition is whether
        the window of substring from s cover all letters in t.
        """

        # Step 1. Get counter of t
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # Step 2. Initialize setup e,g, counter of s, number of 
        # letters need to match
        have = {} # Counter of substring
        need_cnt = len(need) # Number of letters need to match in t
        have_cnt = 0
        min_window_len = float('inf') # Minimum length of substring
        min_window = ""
        n = len(s)
        slow = fast = 0

        # Step 3. Loop s by slow and fast pointers
        while fast < n:

            char = s[fast]

            have[char] = have.get(char, 0) + 1

            if have.get(char) == need.get(char):
                have_cnt += 1

            while have_cnt == need_cnt:
                # Check minimum substring
                if (fast - slow + 1) < min_window_len:
                    min_window = s[slow:fast+1]
                    min_window_len = (fast - slow + 1)
                # Condition match, try to shrink window
                old_char = s[slow]
                # 當 old_char 是 t 的字母，且數字一樣時，要減少
                have[old_char] = have[old_char] - 1
                if old_char in need and have[old_char] < need[old_char]:
                    have_cnt -= 1
                slow += 1

            fast += 1

        return min_window


# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
res = Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
print(res)

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
res = Solution().minWindow(s = "a", t = "a")
print(res)

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
res = Solution().minWindow(s = "a", t = "aa")
print(res)

# Example 4:
# Input: s = "ab", t = "a"
# Output: ""
res = Solution().minWindow(s = "ab", t = "a")
print(res)