class Solution:
    def minChanges(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if i % 2 == 1:
                if s[i] != s[i-1]:
                    cnt += 1
        return cnt