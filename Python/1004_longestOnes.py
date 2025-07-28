from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Iterate starts from zero index of nums and count
        how many 1 in consecutive. 
        
            If nums[i]=0 and k>0, k-1 and cnt+1
            If nums[i]=0 and k=0, can not keep consecutive, cnt=1 and k=k-1

        Edge cases:

            1. Is nums[i] either 0 or 1 ?
            2. Can k == 0 ?

        Compexity:
        * Time O(n)
        * Space O(1)
        """
        cnt = 0
        max_cnt = 0
        copy_k = k
        for i in range(len(nums)):
            # Case 1: Normal consecutive
            if nums[i] == 1:
                print("case1")
                cnt += 1
            # Case 2: Flip to be consecutive
            elif nums[i] == 0 and copy_k > 0:
                print("case2")
                cnt += 1
                copy_k -= 1
            # Case 3: No consecutive, new start if copy_k > 0
            elif nums[i] == 0 and copy_k <= 0:
                print("case3")
                cnt = 0
                copy_k = k
                if copy_k > 0:
                    print("case3+1")
                    cnt += 1
                    copy_k -= 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt
    
class Solution:
    def longestOnes(self, nums, k):
        l, r = 0, 0
        max_cnt = 0
        zero_cnt = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_cnt += 1
            # Find maximum consecutive subarray
            while zero_cnt > k:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            max_cnt = max(max_cnt, r-l+1)
            r += 1
        return max_cnt

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
res = Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
print(res)

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
res = Solution().longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
print(res)

# Example 3:
# Input: nums = [0], k = 0
# Output: 0
res = Solution().longestOnes(nums = [0], k = 0)
print(res)
