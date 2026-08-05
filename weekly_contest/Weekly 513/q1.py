class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:

        def getGCD(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def getStrength(a: int, b: int) -> int:
            gcd = getGCD(a, b)
            return (a // gcd) * (b // gcd)

        ans = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans = max(ans, getStrength(nums[i], nums[j]))

        return int(ans)