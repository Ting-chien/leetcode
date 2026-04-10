from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.backtrack(0, nums, [], res)
        return res

    def backtrack(self, start: int, nums: List[int], path: List[int], res: List[int]) -> None:

        res.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(i+1, nums, path, res)
            path.pop()


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums: List[int], path: List[int] = []):
            # add subset to res
            res.append(path)
            # iterate through nums
            for i in range(len(nums)):
                backtrack(nums[i+1:], path+[nums[i]])
        backtrack(nums)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1,2,3]))