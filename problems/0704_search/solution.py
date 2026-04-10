from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12], 9))
    print(sol.search([-1,0,3,5,9,12], 2))