class Solution1:
    def countRotations(self, s: str, k: int) -> int:

        l = list(s)

        ans = 0
        for _ in range(len(s)):
            # Count score
            score = 0
            for i in range(1, len(s)):
                if l[i] == l[i-1]:
                    score += 1
            if score == k:
                ans += 1
            # Rotate
            l.append(l.pop(0))

        return ans


class Solution2:
    def countRotations(self, s: str, k: int) -> int:

        # Duplicate the string 
        N = len(s)
        s += s

        # Find the initial score
        score = 0
        for i in range(1, N-1):
            if s[i] == s[i-1]:
                score += 1

        # Moving window with length N to find score of each substring
        ans = 0
        for i in range(N):
            if score == k:
                ans += 1
            if s[i] == s[i+1]:
                score -= 1
            if s[i] == s[i+N-1]:
                score += 1

        return ans