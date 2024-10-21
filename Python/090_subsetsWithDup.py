from typing import List


class Solution1:
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
    
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
	
        nums.sort()
        ans = [[]]
        
        for num in nums:
            for index in range(len(ans)):
                temp = ans[index] + [num]
                if temp not in ans:
                    ans.append(temp)
        return ans
    

class Solution3:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """2024/10/21"""
        # sort nums before recursion start
        nums.sort()

        res = []
        def dfs(nums: List[int], path: List[int] = []):
            """
            :param nums: Remain numbers
            :param path: Current subset
            """
            res.append(path)
            for i in range(len(nums)):
                # continue if current number is equal to the previous one
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path+[nums[i]])

        dfs(nums)
        return res
    

if __name__ == '__main__':

    sol = Solution3()
    print(sol.subsetsWithDup([1, 2, 2]))
    print(sol.subsetsWithDup([0]))