from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if i > 0:
                if nums[i] == "_":
                    break
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    nums.append("_")
                    continue
            i += 1
        k = 0
        for num in nums:
            if num == "_":
                break
            k += 1
        return k
    

if __name__ == '__main__':
     sol = Solution()
     print(sol.removeDuplicates(nums=[1, 1, 2]))
     print(sol.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))