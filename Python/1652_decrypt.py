from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        if k == 0:
            return [0] * N
        elif k > 0:
            ans = []
            for i in range(len(code)):
                l_ptr = 0 if i+1+k-N < 0 else i+1+k-N
                r_ptr = i+1+k
                ans.append(sum(code[:l_ptr])+sum(code[i+1:r_ptr]))
            return ans
        else:
            ans = []
            for i in range(len(code)):
                l_ptr = i+k if i+k >= 0 else 0
                r_ptr = i+k+N
                left = code[l_ptr:i]
                right = code[r_ptr:]
                print(left, right)
                ans.append(sum(code[l_ptr:i])+sum(code[r_ptr:]))
            return ans
        

# Example 1:
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
res = Solution().decrypt(code = [5,7,1,4], k = 3)
print(res)

# Example 3:
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
res = Solution().decrypt(code = [2,4,9,3], k = -2)
print(res)
