from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Iterate through nums, and store current max in a variable.
        If nums[i] > current, cnt+1 and current max = nums[i].
        
        Return True if cnt >= 3 else False
        """
        cnt = 0
        max_val = nums[0]
        for num in nums:
            print(f"max_val={max_val}, cnt={cnt}")
            if num > max_val:
                cnt += 1
                max_val = num
            # Check if nums[i] < nums[j] < nums[k]
            if cnt >= 3:
                return True
        return False
    
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1, min2 = float("inf"), float("inf")
        for num in nums:
            # print(f"min1={min1}, min2={min2}")
            if num > min2:
                return True
            elif num < min2 and num > min1:
                min2 = num
            elif num < min1:
                min1 = num
        return False
    

# # Example 1:
# # Input: nums = [1,2,3,4,5]
# # Output: true
# res = Solution().increasingTriplet(nums = [1,2,3,4,5])
# print(res)

# # Example 2:
# # Input: nums = [5,4,3,2,1]
# # Output: false
# res = Solution().increasingTriplet(nums = [5,4,3,2,1])
# print(res)

# # Example 3:
# # Input: nums = [2,1,5,0,4,6]
# # Output: true
# res = Solution().increasingTriplet(nums = [2,1,5,0,4,6])
# print(res)

# Example 4:
# Input: nums = [8,3,2,4,0,5]
# Output: true
res = Solution().increasingTriplet(nums = [8,3,2,4,0,5])
print(res)

