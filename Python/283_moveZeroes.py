from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use two pointers two iterate through nums
        # and find if two nums need to be swapped
        l, r = 0, 0
        N = len(nums)
        
        # Start from left pointer until we find zero 
        while l < N:
            if nums[l] == 0:
                # Move right pointer from left pointer position and try to 
                # find a non zero element
                r = l
                while r < N:
                    if nums[r] != 0:
                        nums[l], nums[r] = nums[r], nums[l]
                        break
                    r += 1
            l += 1

        return nums

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        length=len(nums)
        while i<length:
            if nums[i]==0:
                nums.append(nums.pop(i))
                length-=1
            else:
                i+=1            
        return nums


# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
res = Solution().moveZeroes(nums = [0,1,0,3,12])
print(res)

# Example 2:
# Input: nums = [0]
# Output: [0]
res = Solution().moveZeroes(nums = [0])
print(res)

# Example 3:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
res = Solution().moveZeroes(nums = [0,1,0,3,12,0])
print(res)