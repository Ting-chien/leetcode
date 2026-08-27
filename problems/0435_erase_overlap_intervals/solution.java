import java.util.Arrays;

public class solution {
    public static void main(String[] args) {

        Solution1 solution1 = new Solution1();

        // Test Case 1:
        int[][] intervals1 = {{1,2},{2,3},{3,4},{1,3}}; // Output: 1
        System.out.println(solution1.eraseOverlapIntervals(intervals1));

        // Test Case 2:
        int[][] intervals2 = {{1,2},{1,2},{1,2}}; // Output: 2
        System.out.println(solution1.eraseOverlapIntervals(intervals2));

        // Test Case 3:
        int[][] intervals3 = {{0,2},{1,3},{2,4},{3,5},{4,6}}; // Output: 2
        System.out.println(solution1.eraseOverlapIntervals(intervals3));
    }
}


/**
 * 
 * Solution1: Solve by sorting endTime of intervals
 * Time: O(n)
 * Space: O(1)
 */
class Solution1 {
    public int eraseOverlapIntervals(int[][] intervals) {
        
        // Sort intervals by endTime
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        // Iterate intervals and filter overlapping intervals
        int cnt = 0;
        int prevStart = intervals[0][0], prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int currStart = intervals[i][0], currEnd = intervals[i][1];
            if (currStart < prevEnd) {
                // Skip this interval if overlapping
                cnt += 1;
            } else {
                // Move to the next interval
                prevStart = currStart;
                prevEnd = currEnd;
            }
        }

        return cnt;
    }
}