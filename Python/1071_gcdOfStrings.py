from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        GCD of string 的概念為 str1 和 str2 都可以被 X 整除，代表
        
            str1 = X * m
            str2 = X * n
            
        所以可以知道 X 長度必為 str1, str2 的最大公因數。
        """
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
    

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
res = Solution().gcdOfStrings(str1 = "ABCABC", str2 = "ABC")
print(res)

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
res = Solution().gcdOfStrings(str1 = "ABABAB", str2 = "ABAB")
print(res)