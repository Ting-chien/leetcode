class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # 取出 n 的最低為並加到 res 的最高位裡
            res = (res << 1) | (n & 1)
            # 將 n 向右移一位
            n >>= 1
        return res
    

# Example 1:
# Input: n = 43261596
# Output: 964176192
res = Solution().reverseBits(n=43261596)
print(res)
