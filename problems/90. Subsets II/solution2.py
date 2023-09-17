from typing import List


class Solution:
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