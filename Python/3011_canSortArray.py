from typing import List


class Solution:
    def get_num_of_set(self, num: int):
        num_of_set = 0
        while num:
            # 檢查 num 的二進位最右側是否為 1
            if num & 1:
                num_of_set += 1
            # 將二進位的 num 從右側移除一個數
            num >>= 1
        return num_of_set

    def canSortArray(self, nums: List[int]) -> bool:
        slow, fast = 0, 1
        while fast <= len(nums):
            # 如果不一樣，就將前面 set bit 數量一樣的數字做排列
            if fast == len(nums) or self.get_num_of_set(nums[fast]) != self.get_num_of_set(nums[fast-1]):
                nums[slow:fast] = sorted(nums[slow:fast])
                slow = fast
            # 如果相鄰兩個數字的 set bit 數量一致，則先不動作
            fast += 1
        # 檢查排序完的 nums 是否真的有小到大排列
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
            
        return True


# Example 1:
# Input: nums = [8,4,2,30,15]
# Output: true
res = Solution().canSortArray([8,4,2,30,15])
print(res)

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: true
res = Solution().canSortArray([1,2,3,4,5])
print(res)

# Example 3:
# Input: nums = [3,16,8,4,2]
# Output: false
res = Solution().canSortArray([3,16,8,4,2])
print(res)