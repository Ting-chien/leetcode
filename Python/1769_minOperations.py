from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if boxes[j] == "1":
                    cnt += abs(i-j)
            ans.append(cnt)
        return ans
    

# Example 1:
# Input: boxes = "110"
# Output: [1,1,3]
res = Solution().minOperations(boxes="110")
print(res)

# Example 2:
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
res = Solution().minOperations(boxes = "001011")
print(res)