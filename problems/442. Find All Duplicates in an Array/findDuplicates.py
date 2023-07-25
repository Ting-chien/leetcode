from typing import List


class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        d = {}
        res = []

        for n in nums:
            if n in d:
                d[n] = True
                res.append(n)
            else:
                d[n] = False

        return res
    
class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []
        sorted_nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                res.append(sorted_nums[i])

        return res
    

if __name__ == '__main__':

    sol = Solution2()

    # Test case 1
    nums = [4,3,2,7,8,2,3,1]
    output = sol.findDuplicates(nums)
    print(output)

    # Test case 2
    nums = [1, 1, 2]
    output = sol.findDuplicates(nums)
    print(output)

    # Test case 3
    nums = [1]
    output = sol.findDuplicates(nums)
    print(output)
