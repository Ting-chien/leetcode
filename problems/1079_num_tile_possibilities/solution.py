class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Permutation for letters in tiles, letters might 
        be duplicated.
        """
        N = len(tiles)
        res = set()
        def dfs(reamin: str, curr: str = ""):
            """
            Use dfs to get all permutations

            Args:
                remain: Remain tiles
                curr: Current permutation
            """
            res.add(curr)
            if len(reamin) == 0:
                return
            for i in range(len(reamin)):
                dfs(reamin[:i]+reamin[i+1:], curr+reamin[i])
        dfs(tiles)
        return len(res) - 1
    

# Example 1:
# Input: tiles = "AAB"
# Output: 8
res = Solution().numTilePossibilities(tiles = "AAB")
print(res)

# Example 2:
# Input: tiles = "AAABBC"
# Output: 188
res = Solution().numTilePossibilities(tiles = "AAABBC")
print(res)

# Example 3:
# Input: tiles = "V"
# Output: 1
res = Solution().numTilePossibilities(tiles = "V")
print(res)