'''
Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array which 
gives the sum of zero.

Related topics: Array, Two Pointers

Similar questions: 3Sum closet, 4Sum, 3Sum smaller
'''
class Solution:
    def threeSum(self, nums):
        """
        Method:Pointers
        Complexity: 
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if (i == 0 or nums[i] != nums[i-1]):
                target = 0 - nums[i]
                left = i+1
                right = len(nums) - 1
                while left != right:
                    if (nums[left] + nums[right] == target):
                        res.append([nums[i], nums[left], nums[right]])
                        while left < right:
                            left += 1
                            if nums[left] != nums[left-1]:
                                break
                        while right > left:
                            right -= 1
                            if nums[right] != nums[right+1]:
                                break
                    elif (nums[left] + nums[right] > target):
                        right -= 1
                    elif (nums[left] + nums[right] < target):
                        left += 1

        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))