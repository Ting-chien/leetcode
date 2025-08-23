class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        We can parse bit from least significant bit, check value of
        LSB of a and b after XOR. If the value && LSB of c is 1,
        then no flip is need, if value && LSB is 0, then flip abs(a+b-c) times.
        """
        flips = 0
        while a > 0 or b > 0 or c > 0:
            lsb_a, lsb_b, lsb_c = a & 1, b & 1, c & 1
            # 一般來說 & 優先序大於 |，因此要加上掛號避免運算順序出錯
            if (lsb_a | lsb_b) & lsb_c == 0:
                # 代表 a || b 的 lsb 需要 flip 就為 c 的 lsb
                # If lsb_a=1, lsb_b=1, lsb_c=0 => flip 2
                # If lsb_a=1, lsb_b=0, lsb_c=0 => flip 1
                # If lsb_a=0, lsb_b=1, lsb_c=0 => flip 1
                # If lsb_a=0, lsb_b=0, lsb_c=1 => flip 1
                flips += abs(lsb_a + lsb_b - lsb_c)
            # Shift right by one
            a = a >> 1
            b = b >> 1
            c = c >> 1
            print(f"a={a}, b={b}, c={c}")

        return flips
    

# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
res = Solution().minFlips(a = 2, b = 6, c = 5)
print(res)

# Example 2:
# Input: a = 8, b = 3, c = 5
# Output: 3
"""
a = 1000
b = 0011
c = 0101
"""
res = Solution().minFlips(a = 8, b = 3, c = 5)
print(res)
