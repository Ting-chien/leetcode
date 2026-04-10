from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        
        # Count frequency of each letter
        counter = Counter(s)

        # Iterate through each appears letter and its frequency
        res = 0
        for freq in counter.values():
            if freq % 2 == 0:
                # 如果出現的次數是偶數，則最後一定會剩下兩個字符
                res += 2
            else:
                # 如果出現的次數是奇數，則最後一定會剩下一個字符
                res += 1
        
        return res
    

# Example 1:
# Input: s = "abaacbcbb"
# Output: 5
res = Solution().minimumLength("abaacbcbb")
print(res)

# Example 2:
# Input: s = "aa"
# Output: 2
res = Solution().minimumLength("aa")
print(res)