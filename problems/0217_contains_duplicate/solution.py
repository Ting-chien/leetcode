from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 計算每個數字出現的次數
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        # 檢查是否有數字出現兩次以上
        return any([(val > 1) for val in counter.values()])