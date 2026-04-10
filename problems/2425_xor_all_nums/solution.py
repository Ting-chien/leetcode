from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Get lengths of arrays
        len1, len2 = len(nums1), len(nums2)

        # Dictionary to store frequency of each number
        freq = {}

        # Add frequencies for nums1 elements
        # Each element appears n2 times in final result
        for num in nums1:
            freq[num] = freq.get(num, 0) + len2

        # Add frequencies for nums2 elements
        # Each element appears n1 times in final result
        for num in nums2:
            freq[num] = freq.get(num, 0) + len1

        # XOR numbers that appear odd number of times
        ans = 0
        for num in freq:
            if freq[num] % 2:
                ans ^= num

        return ans


# Example 1:
# Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
# Output: 13
res = Solution().xorAllNums([2,1,3], [10,2,5,0])
print(res)

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 0
res = Solution().xorAllNums([1,2], [3,4])
print(res)