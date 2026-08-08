class Solution {
    /**
     * Use two pointers to expand from center, the center can be any location
     * on the string.
     * @param s
     * @return
     */
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count = count + countPalindrom(s, i, i); // odd
            count = count + countPalindrom(s, i, i+1); // even
        }
        return count;
    }

    /**
     * Use two pointers to travel from center to whole string
     * @param s
     * @return
     */
    private int countPalindrom(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            count ++;
            left --;
            right ++;
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
