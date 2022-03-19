from typing import List

class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # Make first iteration of two list
        hash_nums = {}
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in hash_nums:
                    hash_nums[sum] += 1
                else:
                    hash_nums[sum] = 1

        # Check if the result match the last two list
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                target = 0 - num3 - num4
                if target in hash_nums:
                    count += hash_nums[target]

        return count


class Solution2:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # Make first iteration of two list
        hash_nums = {}
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                hash_nums[sum] = hash_nums.get(sum, 0) + 1

        # Check if the result match the last two list
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                target = 0 - num3 - num4
                count += hash_nums.get(target, 0)

        return count


if __name__ == '__main__':
    sol = Solution2()
    print(sol.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))