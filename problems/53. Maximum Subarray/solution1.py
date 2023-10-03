from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """List all possible subarray and pick max sum"""
        max_sum = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[i:j+1]
                max_sum = sum(arr) if sum(arr) > max_sum else max_sum
        return max_sum
    

if __name__ == '__main__':

    sol = Solution()

    # Test1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))

    # Test1
    nums = [1]
    print(sol.maxSubArray(nums))

    # Test1
    nums = [5,4,-1,7,8]
    print(sol.maxSubArray(nums))