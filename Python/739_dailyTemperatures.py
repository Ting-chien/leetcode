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
        For example,

            temperatures = [73,74,75,71,69,72,76,73]
            res = [0,0,0,0,0,0,0,0]

            i=0, temp=73, stack=[]
            i=1, temp=74, stack=[0]
                prev_index=0, res=[1,0,0,0,0,0,0,0]
            i=2, temp=75, stack=[1]
                prev_index=1, res=[1,1,0,0,0,0,0,0]
            i=3, temp=71, stack=[2]
            i=4, temp=69, stack=[2,3]
            i=5, temp=72, stack=[2,3,4]
                prev_index=4, res=[1,1,1,0,0,0,0,0]
                prev_index=3, res=[1,1,2,0,0,0,0,0]
            i=6, temp=76, stack=[2,5]
                prev_index=5, res=[1,1,3,0,0,0,0,0]
                prev_index=2, res=[1,1,4,0,0,0,0,0]
            i=7, temp=73, stack=[6]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []  # 存 index，棧內溫度遞減

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res
    
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
res = Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
print(res)