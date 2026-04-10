from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        # Create a map to store letter's appearance
        exist = {}

        # Iterate through A and B
        res = []
        curr = 0
        for a, b in zip(A, B):
            if a in exist:
                curr += 1
            else:
                exist[a] = True
            if b in exist:
                curr += 1
            else:
                exist[b] = True
            res.append(curr)

        return res
    

# Example 1:
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
res = Solution().findThePrefixCommonArray([1,3,2,4], [3,1,2,4])
print(res)