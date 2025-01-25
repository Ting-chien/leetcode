from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        Intuition:
        1. Iterate through the whole by two index `slow` and `fast`
        2. If we found nums[slow] < nums[fast] and abs(nums[slow] - nums[fast]), switch their position
        3. If there is no element match the condition in rule above, move index `slow` 1 step
        """
        N = len(nums)
        slow = 0
        while slow < N:
            slow_num = nums[slow]
            fast = slow + 1
            while fast < N:
                fast_num = nums[fast]
                if fast_num < slow_num and abs(fast_num-slow_num) <= limit:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    fast = slow + 1
                    continue
                fast += 1
            slow += 1
        return nums


class Solution2:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        Intuition:
        1. We know that two number can be swapped if substraction between them is smaller
        or equal to limit.
        2. Also, a group of number can be rearranged if any two number can be swapped, and
        this is called transitive swap.
        3. Hence, we reaarange `nums` in ascending order, and iterate through all elements
        to check if each two elements' difference is within limit. If it is, numbers are
        belong to same group.
        4. In the end, we can rearrange the array by group.
        """
        # 找出每一組可被排序的數字
        sorted_nums = sorted(nums)
        num_to_group = {} # 紀錄每個數字的組別
        group_to_nums = {} # 紀錄每個組別的數字
        start = 0
        group = 0
        print(f"sorted_nums: {sorted_nums}")
        for i in range(len(sorted_nums)):
            if i > 0 and abs(sorted_nums[i] - sorted_nums[i-1]) > limit:
                group_to_nums[group] = sorted_nums[start:i]
                start = i
                group += 1
                num_to_group[sorted_nums[i]] = group
            if i==len(sorted_nums)-1:
                group_to_nums[group] = sorted_nums[start:i+1]
                num_to_group[sorted_nums[i]] = group
            else:
                num_to_group[sorted_nums[i]] = group
        print(f"num_to_group: {num_to_group}")
        print(f"group_to_nums: {group_to_nums}")

        # 接著在遍歷一次 nums，並從該位置的數字找到組別，再將該組數字按順序填入
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_nums[group].pop(0)

        return nums

    

# Example 1:
# Input: nums = [1,5,3,9,8], limit = 2
# Output: [1,3,5,8,9]
res = Solution2().lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2)
print(res)

# Example 2:
# Input: nums = [1,7,6,18,2,1], limit = 3
# Output: [1,6,7,18,1,2]
res = Solution2().lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3)
print(res)

# Example 3:
# Input: nums = [1,7,28,19,10], limit = 3
# Output: [1,7,28,19,10]
res = Solution2().lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3)
print(res)