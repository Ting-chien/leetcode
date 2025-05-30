from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
    

"""
nums = [1, 3, 5, 6], target = 4

nums    1,  3,  5,  6
idx     0   1   2   3
left            ^
right       ^
mid             ^

res=left=2
"""