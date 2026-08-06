import java.util.HashMap;
import java.util.Map;


class Solution {

    private int[] coins;
    private int MAX_INF = 1_000_000;
    private Map<String, Integer> memo;

    public int coinChange(int[] coins, int amount) {
        this.coins = coins;
        this.memo = new HashMap<>();
        int ans = dfs(coins.length-1, amount);
        return ans < MAX_INF ? ans : -1;
    }

    private int dfs(int i, int remain) {
        // Early return if result found in memo
        String key = i + "," + remain;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        // If no coins to use
        if (i < 0) {
            return remain == 0 ? 0 : MAX_INF;
        }
        int ans;
        if (coins[i] > remain) {
            // If no capacity
            ans = dfs(i-1, remain);
        } else {
            // Choose or not
            ans = Math.min(dfs(i-1, remain), dfs(i, remain-coins[i])+1);
        }
        // Update memo
        memo.put(key, ans);
        return ans;
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
