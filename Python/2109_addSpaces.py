from typing import List


class Solution1:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        shift = 0
        for i in range(len(s)):
            if i in spaces:
                s = s[:i+shift] + " " + s[i+shift:]
                shift += 1
        return s
    

class Solution2:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = s[:spaces[0]] + " "
        for i in range(1, len(spaces)):
            ans += s[spaces[i-1]:spaces[i]] + " "
        ans += s[spaces[-1]:]
        return ans
    

# Example 0.
# Input: s = "EnjoyYourCoffee", spaces = [5, 9]
# Output: "Enjoy Your Coffee"
res = Solution2().addSpaces(s = "EnjoyYourCoffee", spaces = [5, 9])
print(res)

# Example 1:
# Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
# Output: "Leetcode Helps Me Learn"
res = Solution2().addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15])
print(res)