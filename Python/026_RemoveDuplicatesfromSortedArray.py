'''
Given a sorted array nums, remove the duplicates in-place such 
that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.

Related topic: Array, Two pointers

Similar questions: Remove element, Remove duplcates II
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]

        return count+1

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2]))