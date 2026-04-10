from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Find the max value in candies, and check if each candies[i]+extraCandies
        will be the greatest value
        """
        max_num_of_candies = max(candies)
        res = []
        for c in candies:
            res.append(True if c + extraCandies >= max_num_of_candies else False)
        return res
    

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
res = Solution().kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
print(res)