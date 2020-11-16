'''
Given an array nums of n integers and an integer target, find three 
integers in nums such that the sum is closest to target. Return the 
sum of the three integers. You may assume that each input would have 
exactly one solution.

Related topics: Array, Two pointers

Similar questions: 3Sum, 3Sum smaller
'''
class Solution:

    def mySolution1(self, nums, target):

        min_value = math.inf
        res = 0
        nums.sort()

        for i in range(len(nums) - 2):
            if (i == 0 or nums[i] != nums[i-1]):
                remain = target - nums[i]
                lhs_pointer = i + 1
                rhs_pointer = len(nums) - 1
                while lhs_pointer != rhs_pointer:
                    if remain == (nums[lhs_pointer] + nums[rhs_pointer]):
                        return target
                    else:
                        if abs(remain - (nums[lhs_pointer] + nums[rhs_pointer])) < min_value:
                            min_value = abs(remain - (nums[lhs_pointer] + nums[rhs_pointer]))
                            res = nums[i] + nums[lhs_pointer] + nums[rhs_pointer]
                        if (nums[lhs_pointer] + nums[rhs_pointer]) > remain:
                            rhs_pointer -= 1
                        elif (nums[lhs_pointer] + nums[rhs_pointer]) < remain:
                            lhs_pointer += 1
                            
        return res

    def threeSumClo(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        min_diff = float("inf")
        for i in range(len(nums)-2):
            if (i == 0 or nums[i] != nums[i-1]):
                left = i+1
                right = len(nums) - 1
                while left < right:
                    temp_res = nums[i] + nums[left] + nums[right]
                    temp_diff = abs(temp_res - target)
                    if temp_diff < min_diff:
                        min_diff = temp_diff
                        res = temp_res
                    if temp_res > target:
                        right -= 1
                    elif temp_res < target:
                        left += 1
                    else:
                        return target

        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClo([-1, 2, 1, -4], 1))
    print(sol.threeSumClo([1, 1, 1, 0], 100))
    print(sol.threeSumClo([0,2,1,-3], 1))