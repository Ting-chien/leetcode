class Solution:
    def sumDecoded(self, nums: list[int]) -> int:

        ans = 0
        mod = 10**9 + 7

        for num in nums:

            width = num % 10
            d = str(num // 10)
            x = int(d[:width])
            y = int(d[width:])

            ans += pow(x, y, mod)

        return ans % mod