class Solution {
    public String longestPalindrome_1(String s) {
        // Use two for loop to get all substring,
        // and check whether the substring is palindrome
        int n = s.length();
        String res = "";

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n+1; j++) {
                String subString = s.substring(i, j);
                String reversedSubString = new StringBuilder(subString).reverse().toString();
                if (subString.equals(reversedSubString) && subString.length() > res.length()) {
                    res = subString;
                }
            }
        }

        return res;
    }

    private String getLongestPalindrome(String s, int i, int j) {
        // Get longest length of palindrom from start
        // points i, j
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i --;
            j ++;
        }
        return s.substring(i+1, j);
    }

    public String longestPalindrome_2(String s) {
        // Try to use two pointers to expand
        String res = "";
        for (int i=0; i<s.length(); i++) {
            // Get length when odd
            String p1 = getLongestPalindrome(s, i, i);
            if (p1.length() > res.length()) {
                res = p1;
            }
            // Get length when even
            String p2 = getLongestPalindrome(s, i, i+1);
            if (p2.length() > res.length()) {
                res = p2;
            }
        }
        return res;
    }

    public String longestPalindrome_3(String s) {
        // Initialize a dp matrix
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        // Set value on diagnose to True
        for (int i=0; i<n; i++) {
            dp[i][i] = true;
        }
        // Go through the upper-right of matrix, starting
        // from the most bottom-left position
        String res = "";
        for (int i=n-1; i>=0; i--) {
            for (int j=i; j<n; j++) {
                if (s.charAt(i) == s.charAt(j) && ((j-i) < 3 || dp[i+1][j-1])) {
                    dp[i][j] = true;
                    if ((j - i + 1) > res.length()) {
                        res = s.substring(i, j+1);
                    }
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // Test case 1
        String s1 = "babad";
        String r1 = s.longestPalindrome_3(s1);
        System.out.println("Test 1 result: " + r1);

        // Test case 2
        String s2 = "aaaa";
        String r2 = s.longestPalindrome_3(s2);
        System.out.println("Test 2 result: " + r2);
    }
}