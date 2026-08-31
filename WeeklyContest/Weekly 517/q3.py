class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:

        # 建立一個二維陣列 dp[i][s] 代表前 i 個元素可以組合出 s 的最小執行次數
        dp = [[float('inf')] * (sum + 1) for _ in range(len(nums) + 1)]

        # 當 sum == 0 且沒有任何元素可用時，執行的次數為 0
        dp[0][0] = 0

        # 遍歷每一個 nums 長度以及 sum，並在其中找到適合的 operations
        for i in range(1, len(nums)+1):

            options = []
            num = nums[i-1]

            # Get multiplication options
            x = num
            steps = 0
            while x <= sum:
                options.append((x, steps))
                x *= 2
                steps += 1

            # Get division options
            x = num
            steps = 0
            while x > 0:
                if x <= sum and x > 0:
                    options.append((x, steps))
                x //= 2
                steps += 1

            for j in range(sum+1):
                
                # 不使用第 i 個 element
                dp[i][j] = dp[i - 1][j]

                # 使用第 i 個 element
                for val, cost in options:
                    if val <= j:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i - 1][j - val] + cost # 使用第 i 個 element 轉換為 val 的執行次數
                        )


        return -1 if dp[len(nums)][sum] == float('inf') else dp[len(nums)][sum]

                
if __name__ == "__main__":

    solution = Solution()

    # Test case 1
    print(solution.minOperations(nums = [5,6,10], sum = 4)) # Expected output: 3

    # Test case 2
    print(solution.minOperations(nums = [10,2], sum = 13)) # Expected output: 3

    # Test case 3
    print(solution.minOperations(nums = [6,3], sum = 8)) # Expected output: -1