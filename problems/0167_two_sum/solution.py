from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers where they add up to `target`, and return their
        indices added by one.

        There is exactly one solution in each question, and you may not 
        use same element twice.
        
        Args:
            numbers: 1-indexed integer array sorted in non-decreasing order
            target: Target number
        
        Returns: [index1, index2]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            elif curr < target:
                left += 1
            elif curr > target:
                right -= 1

        
# Example 1
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
ans = Solution().twoSum(numbers=[2,7,11,15], target=9)
print(ans)

# 