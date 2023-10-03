from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Dynamic Programming (bottom up)
        由左往右比對過去的累加總合與當下的值誰比較大
        """
        cur_max = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            max_sum = max(cur_max, max_sum)
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