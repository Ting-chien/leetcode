from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Idea: Hash
        Time Complexity: O(n)
        """
        hash_nums = {}
        for idx, val in enumerate(nums):
            remain = target - val
            if val in hash_nums:
                return [idx, hash_nums[val]]
            hash_nums[remain] = idx


if __name__ == '__main__':

    sol = Solution()

    # Case1
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums, target))

    # Case2
    nums = [3,2,4]
    target = 6
    print(sol.twoSum(nums, target))

    # Case3
    nums = [3,3]
    target = 6
    print(sol.twoSum(nums, target))