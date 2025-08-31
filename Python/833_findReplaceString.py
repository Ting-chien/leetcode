from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        """
        Approach:
        1. Iterate through s and check if index == indices[i]
        2. Check if s[index:index+len(sources[i])] == sources[i]
        3. Put targets[i] into result and move to index+len(sources[i])
        4. Concatenate all string together

        Complexity:
        * Time: O(n)
        * Space: O(n)
        """

        # Turn indices, sources, targets into map for better efficiency
        # in searching exist index
        d = {}
        for index, source, target in zip(indices, sources, targets):
            if s[index:index+len(source)] == source:
                d[index] = (source, target)

        i = 0
        n = len(s)
        result = []
        while i < n:
            # Check if i in indices
            if i in d:
                source, target = d[i]
                # Check if s[i:i+len(source)] == source
                m = len(source)
                if s[i:i+m] == source:
                    # Append new string and jump n indices
                    result.append(target)
                    i += m
                    continue
            # Move one step ahead
            result.append(s[i])
            i += 1
        
        return "".join(result)
    

# Example 2:
# Input: s="abcde", indices=[2,2,3], sources=["cde","cdef","dk"], targets=["fe","f","xyz"]
# Output: "abfe"
res = Solution().findReplaceString(s="abcde", indices=[2,2,3], sources=["cde","cdef","dk"], targets=["fe","f","xyz"])
print(res)
