from typing import List

class Solution1:
    '''
    Iterate
    Time complexity: O(n^2)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            for j in range(i, n):
                new_sum = sum(nums[i:j+1])
                max_sum = new_sum if new_sum > max_sum else max_sum
        return max_sum

class Solution2:
    '''
    DP(Bottom-up)
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        result = [None]*len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = max(result[i-1]+nums[i], nums[i])
        return max(result)

class Solution3:
    '''
    DP(Bottom-up)
    Time complexity: O(n)
    Space complexity: O(1)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = cur_sum
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum+nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum


class Solution4:
    '''
    DP(Top-down) alse known as "divide and conquer"
    Time complexity: O(n)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float('-inf')
        curr_max = 0
        for num in nums:
            if curr_max < 0:
                curr_max = num
            else:
                curr_max += num
            global_max = max(global_max, curr_max)
        return global_max

        

if __name__ == '__main__':
    sol = Solution4()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray([1]))
    print(sol.maxSubArray([5,4,-1,7,8]))