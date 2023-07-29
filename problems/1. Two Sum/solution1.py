from typing import List


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Idea: Two Pointer
        Time Complexity: 
        """

        nums_dict = [[val, index] for index, val in enumerate(nums)]
        nums_dict.sort()
        lhs_pointer, rhs_pointer = 0, len(nums)-1

        while lhs_pointer < rhs_pointer:
            val = nums_dict[lhs_pointer][0] + nums_dict[rhs_pointer][0]
            if val > target:
                rhs_pointer -= 1
            elif val < target:
                lhs_pointer += 1
            else:
                return [nums_dict[lhs_pointer][1], nums_dict[rhs_pointer][1]]
            

if __name__ == '__main__':

    sol = Solution()

    # Case1
    nums = [2,7,11,15]
    target = 9
    assert sol.twoSum(nums, target) == [0, 1]

    # Case2
    nums = [3,2,4]
    target = 6
    assert sol.twoSum(nums, target) == [1, 2]

    # Case3
    nums = [3,3]
    target = 6
    assert sol.twoSum(nums, target) == [0, 1]