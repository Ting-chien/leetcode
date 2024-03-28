from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
    
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    

if __name__ == '__main__':
    sol = Solution()

    # Case1
    nums = [3,2,2,3]
    val = 3
    print(sol.removeElement(nums, val))

    # Case1
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(sol.removeElement(nums, val))