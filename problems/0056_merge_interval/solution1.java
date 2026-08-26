import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class solution1 {
    public int[][] merge(int[][] intervals) {
        // Return if there is only one interval
        if (intervals.length == 1) {
            return intervals;
        }

        // Sort intervals by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        // Get the latest interval
        int currStart = intervals[0][0], currEnd =  intervals[0][1];

        // Iterate through upcoming intervals and concatenate if overlap
        List<int[]> ans = new ArrayList<>();
        for (int i = 1; i < intervals.length; i++) {
            // Check if overlapping
            if (currEnd >= intervals[i][0]) {
                // Update current interval close boundary
                currEnd = Math.max(currEnd, intervals[i][1]);
            } else {
                // Append current interval and switch to new one
                ans.add(new int[]{currStart, currEnd});
                currStart = intervals[i][0];
                currEnd = intervals[i][1];
            }
        }

        // Append the last interval
        ans.add(new int[]{currStart, currEnd});

        // Convert ArrayList to int[][]
        return ans.toArray(new int[ans.size()][]);
    }

    public static void main(String[] args) {

        // Test case 1
        int[][] intervals1 = {{1,3},{2,6},{8,10},{15,18}};
        int[][] result1 = new solution1().merge(intervals1);
        System.out.println(Arrays.deepToString(result1));

        // Test case 2
        int[][] intervals2 = {{1,4},{4,5}};
        int[][] result2 = new solution1().merge(intervals2);
        System.out.println(Arrays.deepToString(result2));
    }
}
