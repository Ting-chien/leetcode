from typing import List


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         N = len(s)
#         slow, fast = N, N-1

#         # Loop while fast index in s
#         while fast >= 0:
#             word = s[fast:slow]
#             if word in wordDict:
#                 slow = fast
#             fast -= 1

#         # If slow == 0, means they found all match segments
#         return slow == 0

class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Limit Exceed
         - Time complexity: O((n*2^n)+m)，n 是 s 的長度，m 是 wordDict 長度。

        """
        # 將 wordDict 轉為 wordSet 轉為 set 需花費 O(m)
        wordSet = set(wordDict)
        # DFS 裡做的是一個 decision tree 的算法，每個字元可以選擇 切 或 不切
        # 舉例，有一字串 abc，總共有
        # "abc", "a" + "bc", "ab" + "c", "a" + "b" + "c"
        # 共 2^(n-1) = 4 種可能。
        # 再加上 s[i:j] 最差為 O(n)，因此是 O(n*2^n)
        def dfs(i):
            """
            Args:
                i: Start index of substring
            
            Return:
                bool
            """
            if i == len(s):
                return True
            # 檢查每組 substring 和剩下的字串是否可被切割為 segments
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and dfs(j):
                    return True
            return False
        return dfs(0)
    

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Memorization
         - Time complexity: 最差情況為遍歷所有 index，每個 j 又遍歷至 len
         所以最差為 O()
        """
        wordSet = set(wordDict)
        memo = [None] * len(s)
        def dfs(i):
            """
            Args:
                i: Start index of substring
            
            Return:
                bool
            """
            if i == len(s):
                return True
            if memo[i] != None:
                return memo[i]
            # 檢查每組 substring 和剩下的字串是否可被切割為 segments
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)
    

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
ans = Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"])
print(ans)

# Example 2:
# Input: s = "aaaaaaa", wordDict = ["aaaa","aaa"]
# Output: true
ans = Solution().wordBreak(s = "aaaaaaa", wordDict = ["aaaa","aaa"])
print(ans)