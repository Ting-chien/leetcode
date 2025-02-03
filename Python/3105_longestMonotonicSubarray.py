from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Intuition
        1. 透過一個變數去紀錄現在是 increase 或 decrease 的變化
        2. 遍歷整個 array，並藉由一個變數 curr 去紀錄當下連去升降冪的數量
        3. 透過一變數 max 來紀錄每一輪結束時相比的最大值
        """
        order = None # asc | desc | None
        max_cnt = 1
        cur_cnt = 1
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    order = None
                    max_cnt = max(max_cnt, cur_cnt)
                    cur_cnt = 1
                elif order == "asc" and nums[i] < nums[i-1]:
                    order = "desc"
                    max_cnt = max(max_cnt, cur_cnt)
                    cur_cnt = 2
                elif order == "desc" and nums[i] > nums[i-1]:
                    order = "asc"
                    max_cnt = max(max_cnt, cur_cnt)
                    cur_cnt = 2
                else:
                    order = "asc" if nums[i] > nums[i-1] else "desc"
                    cur_cnt += 1

        return max(max_cnt, cur_cnt)
    

# Example 1:
# Input: nums = [1,4,3,3,2]
# Output: 2
res = Solution().longestMonotonicSubarray([1,4,3,3,2])
print(res) # 2

# Example 2:
# Input: nums = [3,3,3,3]
# Output: 1
res = Solution().longestMonotonicSubarray([3,3,3,3])
print(res) # 1

# Example 3:
# Input: nums = [3,2,1]
# Output: 3
res = Solution().longestMonotonicSubarray([3,2,1])
print(res) # 3

# Example 4:
# Input: nums = [1,9,7,1]
# Output: 3
res = Solution().longestMonotonicSubarray([1,9,7,1])
print(res) # 3
