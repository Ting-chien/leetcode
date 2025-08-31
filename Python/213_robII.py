from typing import List


class Solution:

    def sequence_dp(self, nums: List[int]) -> int:
        # h1, h2 = nums[0], max(nums[0], nums[1])
        # 因為有可能 len(nums) == 1，因此不能先取好 h1, h2
        h1, h2 = 0, 0
        for i in range(len(nums)):
            h1, h2 = h2, max(h2, h1+nums[i])
        return h2

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        # 將 nums 拆成 nums[1:] 和 nums[:-1] 來避免頭尾都取
        # 然後再比較兩個算出來的結果取大值
        return max(self.sequence_dp(nums[:-1]), self.sequence_dp(nums[1:]))