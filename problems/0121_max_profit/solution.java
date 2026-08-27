

public class solution {
    public static void main(String[] args) {

        Solution1 solution1 = new Solution1();

        // Test Case 1:
        int[] prices = {7, 1, 5, 3, 6, 4}; // Output: 5
        System.out.println(solution1.maxProfit(prices));

        // Test Case 2:
        int[] prices2 = {7, 6, 4, 3, 1}; // Output: 0
        System.out.println(solution1.maxProfit(prices2));
    }
}


/**
 * Solution 1: Brute Force
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
class Solution1 {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = prices[0];
        for (int i = 1; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        return maxProfit;
    }
}