from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Intuition: The maximum possible bitwise AND of
        a subarray would be the maximum number in the array 
        itself. This is because the bitwise AND operation 
        with a larger number and a smaller number would always 
        result in a number less than or equal to the smaller number.
        """
        m_val, curr_l, max_l = 0, 0, 0
        for num in nums:
            if num > m_val:
                # 當發現比 max_val 還大的數值時，將 max value
                # 轉為新的數值，並將當前最大長度和總最大長度都改為 1
                m_val = num
                curr_l = 1
                max_l = 1
            elif num == m_val:
                # 若遇到和當前最大值一樣的數值時，將大錢最大長度 +1
                # 並且檢查當前最大長度和總最大長度誰長
                curr_l += 1
                max_l = max(max_l, curr_l)
            else:
                # 若遇到比當前最大值小的數值時，要重置當前最大長度為 0
                curr_l = 0
        return max_l

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        
        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans
    

if __name__ == "__main__":

    # Example 1
    # Input: nums = [1,2,3,3,2,2]
    # Output: 2
    print(Solution().longestSubarray(nums=[1,2,3,3,2,2]))

    # Example 2
    # Input: nums = [1,2,3,4]
    # Output: 1
    print(Solution().longestSubarray(nums=[1,2,3,4]))
