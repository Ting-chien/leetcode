class Solution1:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s: str) -> str:
            return "".join(["1" if c == "0" else "0" for c in s])
        
        def recursion(n: int) -> str:
            # return if n is 1
            if n == 1:
                return "0"
            return recursion(n-1) + "1" + invert(recursion(n-1))[::-1]
        
        return recursion(n)[k-1]
    

class Solution2:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s: str) -> str:
            return "".join(["1" if c == "0" else "0" for c in s])
        
        dp = ["0"] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + "1" + invert(dp[i-1])[::-1]

        return dp[n][k-1]
    

class Solution3:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s: str) -> str:
            return "".join(["1" if c == "0" else "0" for c in s])
        
        s = "0"
        for _ in range(2, n+1):
            s = s + "1" + invert(s)[::-1]

        return s[k-1]
    

# Example 1:
# Input: n = 3, k = 1
# Output: "0"
res = Solution3().findKthBit(n=3, k=1)
print(res)

# Example 2:
# Input: n = 4, k = 11
# Output: "1"
res = Solution3().findKthBit(n=4, k=11)
print(res)