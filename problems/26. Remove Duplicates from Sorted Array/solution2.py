from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i > 0:
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    continue
            i += 1
        return len(nums)
    

if __name__ == '__main__':
     sol = Solution()
     print(sol.removeDuplicates(nums=[1, 1, 2]))
     print(sol.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))