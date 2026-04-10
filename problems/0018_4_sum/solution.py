'''
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b 
+ c + d = target? Find all unique quadruplets in the array 
which gives the sum of target. Note: The solution set must not contain duplicate quadruplets.

Related topics: Array, Hash Table, Two Pointer

Similar questions: 4Sum II
'''
import collections

class Solution:
    def fourSum(self, nums, target):
        """
        Method: Two pointers
        Complexity: O(n^3)
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, len(nums)-2):
                    if j == i+1 or nums[j] != nums[j-1]:
                        left = j + 1
                        right = len(nums) - 1
                        remain = target - nums[i] - nums[j]
                        while left != right:
                            if remain == nums[left] + nums[right]:
                                res.append([nums[i], nums[j], nums[left], nums[right]])
                                while left < right:
                                    left += 1
                                    if nums[left] != nums[left-1]:
                                        break
                                while right > left:
                                    right -= 1
                                    if nums[right] != nums[right+1]:
                                        break
                            elif nums[left] + nums[right] > remain:
                                right -= 1
                            elif nums[left] + nums[right] < remain:
                                left += 1

        return res

    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                is_duplicated = False
                for [x, y] in lookup[nums[i] + nums[j]]:
                    print(x, y)
                    if nums[x] == nums[i]:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    lookup[nums[i] + nums[j]].append([i, j])
        ans = {}
        for c in range(2, len(nums)):
            for d in range(c+1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = " ".join(str(quad))
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum2([1, 0, -1, 0, -2, 2], 0))