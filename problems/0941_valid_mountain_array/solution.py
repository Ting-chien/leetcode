from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        # mountain array's length should > 3
        if len(arr) < 3: return False

        is_uphill, is_downhill = False, False
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                if is_downhill:
                    return False
                if not is_uphill:
                    is_uphill = True
            elif arr[i-1] > arr[i]:
                if not is_uphill:
                    return False
                if not is_downhill:
                    is_downhill = True
            else:
                return False
            
        return is_uphill and is_downhill
    

# Example 1:
# Input: arr = [2,1]
# Output: false
res = Solution().validMountainArray([2,1])
print(res)

# Example 2:
# Input: arr = [3,5,5]
# Output: false
res = Solution().validMountainArray([3,5,5])
print(res)

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
res = Solution().validMountainArray([0,3,2,1])
print(res)