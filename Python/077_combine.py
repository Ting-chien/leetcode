from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # Make the list
        arr = [x for x in range(1, n+1)]

        # Do the algorithm
        return self.backtrack(arr, 0, [], k, [])

    def backtrack(self, nums: List[int], start: int, res: List[List[int]], k: int, tmp: List[int]):
        # Base case, return if length of tmp equal k
        if len(tmp) == k:
            res.append(tmp.copy())
            return res

        # General case
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.backtrack(nums, i+1, res, k, tmp)
            tmp.pop()

        return res

    
if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4,2))
    print(sol.combine(1,1))