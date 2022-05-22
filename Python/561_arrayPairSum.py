from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0
        for i in range(int(len(sorted_nums)/2)):
            result += sorted_nums[i*2]
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.arrayPairSum([1,4,3,2]))
    print(sol.arrayPairSum([6,2,6,5,1,2]))