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


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1,2,3]))