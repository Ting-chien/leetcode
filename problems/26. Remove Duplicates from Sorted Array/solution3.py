from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # Since there is at least one unique integer
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
    

if __name__ == '__main__':
     sol = Solution()
     print(sol.removeDuplicates(nums=[1, 1, 2]))
     print(sol.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))