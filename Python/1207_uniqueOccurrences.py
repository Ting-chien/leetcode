from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Use a map to store number of occurence of 
        # each value
        counter = {}
        for val in arr:
            if val not in counter:
                counter[val] = 1
            else:
                counter[val] += 1
        # Check if the occurence are unique
        return len(set(counter.values())) == len(counter)
    

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
res = Solution().uniqueOccurrences(arr = [1,2,2,1,1,3])
print(res)

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
res = Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])
print(res)
