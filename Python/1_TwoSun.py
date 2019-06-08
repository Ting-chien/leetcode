'''
Describtion: Given an array of integers, return indices of the two numbers 
such that they add up to a specific target. You may assume that each input 
would have exactly one solution, and you may not use the same element twice.

Related topic: Array, Hash table

Similar questions: 3Sum, 4Sum, TwoSumII, TwoSumIII
'''
class Solution:
    def twoSum(self, nums, target):
        """
        Methods:Array
        Complexity:O(n^2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):  
            complement = target - nums[i]
            for j in range(i+1, len(nums)):#linear search 
                if complement == nums[j]:
                    return [i, j]
        return []

    def twoSum(self, nums, target):
        """
        Methods:Hash
        Complexity:O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))