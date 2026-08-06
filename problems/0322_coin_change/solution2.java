class Solution {
    public int coinChange(int[] coins, int amount) {
        // Initialize a 2D dp talbe
        int MAX_INF = 1_000_000;
        int[][] dp = new int[coins.length+1][amount+1];

        // Give a initial value to amount=0 and coin=0
        for (int i = 0; i <= coins.length; i++) {
            for (int j = 0; j <= amount; j++) {
                dp[i][j] = (j == 0) ? 0 : MAX_INF;
            }
        }

        // Iterate from amount=1 and coin=1
        for (int i = 1; i <= coins.length; i++) {
            for (int j = 1; j <= amount; j++) {
                if (coins[i-1] > j) {
                    // Out of capacity
                    dp[i][j] = dp[i-1][j];
                } else {
                    // Pick or skip
                    dp[i][j] = Math.min(dp[i-1][j], dp[i][j-coins[i-1]]+1);
                }
            }
        }

        return (dp[coins.length][amount] == MAX_INF) ? -1 : dp[coins.length][amount];
    }

    public static void main(String[] args) {

        Solution s = new Solution();

        // Test case 1
        System.out.println(s.coinChange(new int[]{1, 2, 5}, 11)); // 3

        // Test case 2
        System.out.println(s.coinChange(new int[]{2}, 3)); // -1

        // Test case 3
        System.out.println(s.coinChange(new int[]{1}, 0)); // 0

    }
}
