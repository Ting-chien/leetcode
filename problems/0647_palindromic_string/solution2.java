class Solution {
    /**
     * Use two dimension dp to store whether dp[i][j] is palindrom
     * or not. dp[i][j] means s[i..j].
     * @param s
     * @return
     */
    public int countSubstrings(String s) {
        // Initialize a 2D dp with default value is false
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = false;
            }
        }

        // Iterate from small substring
        int count = 0;
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) && ((j - i <= 2) || (dp[i+1][j-1]))) {
                    dp[i][j] = true;
                    count ++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {

        Solution s = new Solution();

        // Test case 1
        System.out.println(s.countSubstrings("abc")); // 3

        // Test case 2
        System.out.println(s.countSubstrings("aaa")); // 6
    }
}
