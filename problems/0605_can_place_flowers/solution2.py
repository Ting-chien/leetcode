from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]

        return count <= 1
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPossibility([4,2,3]))
    print(sol.checkPossibility([4,2,1]))
    print(sol.checkPossibility([3,4,2,3]))
    print(sol.checkPossibility([1,3,2]))