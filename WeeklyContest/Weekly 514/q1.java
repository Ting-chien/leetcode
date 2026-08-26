import java.util.Arrays;

class Solution {
    public double minPrice(int[] prices, int[] discounts) {

        // Sort prices and discounts first
        Arrays.sort(prices);
        Arrays.sort(discounts);

        // Get length of prices and discounts
        int pricesLength = prices.length;
        int discountsLength = discounts.length;

        // Count by price and discount and add upp
        double ans = 0;
        for (int i = pricesLength - 1; i >= 0; i--) {
            if (discountsLength > 0) {
                int p = prices[i];
                int d = discounts[--discountsLength];
                ans += (double) (p * (100 - d)) / 100;
            } else {
                ans += prices[i];
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        
        Solution solution = new Solution();

        // Test case 1
        int[] prices = {10, 30, 21};
        int[] discounts = {50, 60};
        System.out.println(solution.minPrice(prices, discounts));
    }
}