from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Use prefix and postfix to store sum of 
        nums[:i] and nums[i+1:]. If
        
            * prefix == postfix, return index
            * prefix > postfix, return -1
            * prefix < postfix, keep iterate

        Complexity:
        * Space
        * Time
        """
        prefix, postfix = 0, sum(nums)
        for i in range(len(nums)):
            postfix -= nums[i]
            if prefix == postfix:
                return i
            prefix += nums[i]
            print(f"prefix={prefix}, postfix={postfix}")
            # if prefix < postfix:
            #     prefix += nums[i]
            #     continue
            # elif prefix == postfix:
            #     return i
            # else:
            #     return -1
        return -1
            

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
res = Solution().pivotIndex(nums = [1,7,3,6,5,6])
print(res)

# Example 2:
# Input: nums = [2,1,-1]
# Output: 0
res = Solution().pivotIndex(nums = [2,1,-1])
print(res)

# Example 3:
# Input: nums = [-1,-1,-1,-1,-1,0]
# Output: 2
res = Solution().pivotIndex(nums = [-1,-1,-1,-1,-1,0])
print(res)