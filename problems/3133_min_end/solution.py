class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        target = 1
        remain = n - 1
        while remain:
            if not x & 1:
                remain -= 1
            x >>= 1
            target <<= 1
        print(f"result={bin(result)}")
        print(f"target={bin(target)}")
        target >>= 1
        return result | target
    

# Example 1:
# Input: n = 3, x = 4
# Output: 6
res = Solution().minEnd(n=3, x=4)
print(res)

# Example 2:
# Input: n = 2, x = 7
# Output: 15
res = Solution().minEnd(n=2, x=7)
print(res)

# Example 3: Failed
# Input: n = 4, x = 1
# Output: 7
res = Solution().minEnd(n=4, x=1)
print(res) # Output: 9