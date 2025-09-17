class Solution:
    def longestDupSubstring(self, s: str) -> str:

        # Find all possible substrings
        n = len(s)        
        substrings = []
        # def dfs(start: int, path: str):
        #     """
        #     Args:
        #         start: 開始遞迴的位置
        #         path: 當前 substring
        #     """
        #     substrings.append(path)
        #     # Base
        #     if start == n:
        #         return
        #     # General
        #     for i in range(start, n):
        #         dfs(i+1, path+s[i])
        # dfs(0, "")
        for i in range(n):
            for j in range(i, n):
                substrings.append(s[i:j+1])
        print(substrings)
        
        # Count each substring occurence
        counter = {}
        for substring in substrings:
            counter[substring] = counter.get(substring, 0) + 1
        print(counter)

        # Filter all substring with occurence over twice
        high_frequency_substrings = [k for k, v in counter.items() if v > 1]
        print(high_frequency_substrings)

        # Return the longest substring
        return sorted(high_frequency_substrings, key=lambda x: len(x))[-1] if high_frequency_substrings else ""


# Example 1:
# Input: s = "banana"
# Output: "ana"
res = Solution().longestDupSubstring(s="banana")
print(res)