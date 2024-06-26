from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(nums: List[int], arr: List[int]):
            result.append(arr[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                backtrack(nums[i+1:], arr)
                arr.pop()
        backtrack(nums, [])
        return result
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
	
        nums.sort()
        ans = [[]]
        
        for num in nums:
            for index in range(len(ans)):
                temp = ans[index] + [num]
                if temp not in ans:
                    ans.append(temp)
        
        return ans
    

if __name__ == '__main__':

    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 2]))
    print(sol.subsetsWithDup([0]))