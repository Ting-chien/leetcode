from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        spell=[5,1,3](n), potions=[1,2,3,4,5](m), success=7
        
            Our goal is spell[i]*potion[j] >= success

            Return [4, 0, 3]

        Edge cases:
         - Number are all positive integers
         - spell and porion won't be empty
         - Does value repeat ? Does it count ?

        Approach
        1. Iterate through spell, and pick one spell[i]
        2. target = success / spell[i]
            e,g,. spell[i]=5, success=7, potion[j] >= 1.4
        3. Iterate through potions to find how many potions are greater than target,
        or I can use binary search to prevent linear situation

        Complexity
        * Time: O(m*n) - Time Limit Exceeded
        * Space: O(1) - 
        """

        # Sort potions first
        potions.sort()
        M = len(potions)

        pairs = []
        for spell in spells:
            target = success / spell
            j = 0
            while j < M:
                if potions[j] >= target:
                    pairs.append(len(potions[j:]))
                    break
                j += 1
            else:
                pairs.append(len(potions[j:]))

        return pairs
    

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Binary Search Algorithm

            [1,2,3,4*,4,4,5], target=3.1

            Goal: Find the closet number which is greater or equal to target with smallest index

        Complexity:
        * Time: O(nlogm) - beats 30.97%
        * Space: O(n) - beats 45.37%

        Spend: 33:12
        """
        potions.sort()
        m = len(potions)
        pairs = []
        for spell in spells:
            target = success / spell
            left, right = 0, m-1
            while left <= right:
                middle = (left + right) // 2
                if potions[middle] >= target:
                    right = middle - 1
                elif potions[middle] < target:
                    left = middle + 1
            pairs.append(m-left)
        return pairs
    

# Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
res = Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7)
print(res)