from typing import List


class Solution1:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # 將 nums 先排序過
        nums.sort()
        max_beauty = 0
        # 再去尋找 sorted nums 中每一個數字的最大 overlap 範圍
        # 在 overlap 範圍內的數字就會是 maximum subsequence
        for i in range(len(nums)):
            # 找到 overlap 的 upper_bound
            upper_bound = nums[i] + 2*k
            idx = self.b_search(nums, upper_bound)
            # 計算 maximum subsequence
            max_beauty = max(max_beauty, idx-i+1)
        return max_beauty
    def l_search(self, nums, target):
        """Linear Search (Time Limit Exceed)"""
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= target:
                return i
    def b_search(self, nums, target):
        """Binary Search"""
        left, right, result = 0, len(nums) - 1, 0
        while left <= right:
            mid = (left + right) // 2
            # 查詢最接近 target 且 <= target 的數字
            if nums[mid] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
    

class Solution2:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        透過 sliding window 來不斷移動 x + 2k 的 window
        """
        nums.sort()
        max_beauty = 0
        left, right = 0, 0
        while right < len(nums):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            max_beauty = max(max_beauty, right-left+1)
            right += 1
        return max_beauty

            

# Example 1:
# Input: nums = [4,6,1,2], k = 2
# Output: 3
res = Solution2().maximumBeauty(nums = [4,6,1,2], k = 2)
print(res)