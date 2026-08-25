class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:

        # Sort prices and discounts in ascending order
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        # Iterate prices and discounts
        ans = 0
        curr = 0
        for p, d in zip(prices, discounts):
            ans += (p * (100 - d)) / 100
            curr += 1

        ans += sum(prices[curr:])
        return ans


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.minPrice([10, 30, 21], [50, 60])) # Output: 32.50000

    # Test cases 2
    print(solution.minPrice(prices = [100,70], discounts = [10,40,50])) # Output: 92.00000

    # Test cases 3
    print(solution.minPrice(prices = [7,3,9], discounts = [100,100])) # Output: 3.00000