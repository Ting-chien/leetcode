from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        # 一個字串 s 可以組成最多的回文數量為 len(s)，像是 
        # 'abcba' -> 'a', 'a', 'b', 'b', 'c'，所以當
        # len(s) < k 時，則代表不可能組出 k 組回文
        N = len(s)
        if N < k:
            return False
        if N == k:
            return True
        
        # 因為一組回文最多可以有一個出現奇數次的字母，其餘字母
        # 出現的次數皆須為偶數。因此字串 s 可以組出的回文最少
        # 數量為字串中出現次數為奇數的字母數量，像是 'aabbc' -> 'abcba'
        # 或是 'leetcode' -> 'l', 'eee', 't', 'o', 'd'
        # 因此當 k < 奇數的字母，則不可能達成
        counter = Counter(s)
        num_of_odd = 0
        for key, val in counter.items():
            if (val % 2) != 0:
                num_of_odd += 1
        return True if k >= num_of_odd else False

        

# Example 1:
# Input: s = "annabelle", k = 2
# Output: true
res = Solution().canConstruct(s = "annabelle", k = 2)
print(res) # True

# Example 2:
# Input: s = "leetcode", k = 3
# Output: false
res = Solution().canConstruct(s = "leetcode", k = 3)
print(res) # False

# Example 3:
# Input: s = "true", k = 4
# Output: true
res = Solution().canConstruct(s = "true", k = 4)
print(res) # True

# Example 4:
# Input: s = "none", k = 4
# Output: true
res = Solution().canConstruct(s = "none", k = 4)
print(res) # True