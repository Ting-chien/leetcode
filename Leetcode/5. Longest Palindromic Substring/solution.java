class Solution {
    public String longestPalindrome(String s) {
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

    public static void main(String[] args) {
        Solution s = new Solution();

        // Test case 1
        String s1 = "babad";
        String r1 = s.longestPalindrome(s1);
        System.out.println("Test 1 result: " + r1);

        // Test case 2
        String s2 = "aaaa";
        String r2 = s.longestPalindrome(s2);
        System.out.println("Test 2 result: " + r2);
    }
}