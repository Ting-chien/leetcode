from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Intuition
        1. 宣告一 max_val 來紀錄最大的 ascending subarray 和
        2. 從 index=0 開始遍歷 nums，並宣告一 curr_val 來紀錄目前 subarray 的和
            2-1. 如果 nums[i] > nums[i-1]，就將 nums[i] 加到 curr_val
            2-2. 如果 nums[i] <= nums[i-1]，那就比較 max_val 和 curr_val 誰比較大，
            並且將 curr_val=num[i]
        """
        max_val, cur_val = nums[0], nums[0]
        for i in range(len(nums)):
            if i > 0:
                if nums[i] > nums[i-1]:
                    cur_val += nums[i]
                else:
                    max_val = max(max_val, cur_val)
                    cur_val = nums[i]
        return max(max_val, cur_val)