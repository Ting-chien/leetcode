class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Notes
        1. Length of haystack and needle
        2. Can the length of needle longer than haystack ?
        3. All lowercase letters

        Approach
        1. Get the length m, n of haystack and needle
        2. Use index i to iterate through haystack
            2-1. If we find haystack[i] == needle[0], keep comparing 
            until we match haystack[i+n-1] == needle[n-1], return i
            2-2. If mismatch during comparing k times, i += k
        3. Repeat step 2

        Complexity
        * Time: O(n*m)
        * Space: O(1)

        Result: Fail in Example 4 ❌
        
        """
        m, n = len(haystack), len(needle)

        i = 0
        while i < m:
            j = 0
            while haystack[i+j] == needle[j]:
                # If current character in haystack is equal
                # to reference character from needle, then
                # compare next character
                if j == (n-1):
                    return i
                # i += 1
                j += 1
                
            i = (i + 1) if j == 0 else (i + j)

        return -1
    

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Naive string matching

        * Time: O(m*n) ➡️ 時間複雜度差，像 Example 4 就會需要每一輪
        都跑一次 O(n)
        """

        m, n = len(haystack), len(needle)

        i = 0
        while i < m:
            if haystack[i:i+n] == needle:
                return i
            i += 1

        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        嘗試用 KMP 算法將時間複雜度進一步壓縮到 O(n+m)

        Complexity:
        * Time: O(n+m) - n is len(haystack), m is len(needle)
        * 
        """

        m, n = len(haystack), len(needle)

        # Get LPS of string needle
        lps = [0] * n
        prev_lps, i = 0, 1
        while i < n:
            if needle[i] == needle[prev_lps]:
                # Match, update LPS and move one step forward
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            else:
                # Not match, check whether LPS > 0
                if prev_lps == 0:
                    lps[i] = 0
                    i += 1
                else:
                    # If not, find previous LPS
                    prev_lps = lps[prev_lps-1]

        # KMP string match
        i = j = 0 # i: haystack, j: needle
        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return (i - j)
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

        return -1

    

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
res = Solution().strStr(haystack = "sadbutsad", needle = "sad")
print(res)

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
res = Solution().strStr(haystack = "leetcode", needle = "leeto")
print(res)

# Example 3:
# Input: haystack = "leetleeto", needle = "leeto"
# Output: 4
res = Solution().strStr(haystack = "leetleeto", needle = "leeto")
print(res)

# Example 4:
# Input: haystack = "aaa", needle = "aaaa"
# Output: -1
res = Solution().strStr(haystack = "aaa", needle = "aaaa")
print(res)

# Example 4:
# Input: haystack = "aaaaab", needle = "aaab"
# Output: 2
res = Solution().strStr(haystack = "aaaaab", needle = "aaab")
print(res)

