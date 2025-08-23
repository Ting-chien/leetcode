from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use two pointers to iterate through temperatures, slow pointer
        for current temperature and fast pointer for next tempurature.

        ❌ Time Limit Exceeded
        """
        n = len(temperatures)
        res = []
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    cnt = j - i
                    break
            res.append(cnt)
        return res
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        The problem ask us to return an array, which value is the number
        of days to wait for warmer temperature.

        Intuition
        1. Use monotonic stack to find the index of warmer days
        2. Put the diff of two days to the ans array

        Complexity
        * Time: O(n)
        * Space: O(n)
        
        """
        days = len(temperatures)
        ans = [0] * days
        stack = []
        for i in range(days):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans


# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
res = Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
print(res)