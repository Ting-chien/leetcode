class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = set()
        def dfs(remains: str, path: set = set()):
            nonlocal res
            # return if remain characters is empty
            if remains == "":
                # check if number of substring is greater than result
                if len(path) > len(res):
                    res = path
                return
            # go through remain characters
            sub_str = ""
            for i in range(len(remains)):
                sub_str += remains[i]
                if sub_str in path:
                    continue
                dfs(remains[i+1:], path | {sub_str})
        dfs(s)
        return len(res)
        
        
# Example 1:
# Input: s = "ababccc"
# Output: 5
res = Solution().maxUniqueSplit(s="ababccc")
print(res)

# Example 2:
# Input: s = "aba"
# Output: 2
res = Solution().maxUniqueSplit(s="aba")
print(res)

# Example 3:
# Input: s = "aa"
# Output: 1
res = Solution().maxUniqueSplit(s="aa")
print(res)