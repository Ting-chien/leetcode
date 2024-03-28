'''
Describtion: Given an array of integers, return indices of the two numbers 
such that they add up to a specific target. You may assume that each input 
would have exactly one solution, and you may not use the same element twice.

Related topic: Array, Hash table

Similar questions: 3Sum, 4Sum, TwoSumII, TwoSumIII
'''
class Solution:
    def twoSum1(self, nums, target):
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

    def twoSum2(self, nums, target):
        """
        Methods:Hash
        Complexity:O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_nums = {}
        for index, value in enumerate(nums):
            remain = target - value
            if remain in hash_nums:
                return [hash_nums[remain], index]
            hash_nums[value] = index

    def twoSum3(self, nums, target):
        """
        Methods:Two pointers
        Complexity:O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 由小到大先將序列排序
        nums_dict = [[value, index] for index, value in enumerate(nums)]
        nums_dict.sort()
        # 將兩指針從兩側開始定位
        left = 0
        right = len(nums) - 1
        while left < right:
            curr = nums_dict[left][0] + nums_dict[right][0]
            if curr == target:
                return [nums_dict[left][1], nums_dict[right][1]]
            elif curr < target:
                left += 1
            elif curr > target:
                right -= 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum3([2,7,11,15], 9))