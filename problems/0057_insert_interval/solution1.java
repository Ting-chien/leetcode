import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class solution1 {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
        List<int []> ans = new ArrayList<>();
        int idx = 0;

        // Append intervals on the left side of newInterval
        while (idx < intervals.length && intervals[idx][1] < newInterval[0]) {
            ans.add(new int[]{intervals[idx][0], intervals[idx][1]});
            idx++;
        }

        // Aggregate intervals overlap with newInterval
        int newStart = newInterval[0], newEnd = newInterval[1];
        while (idx < intervals.length && intervals[idx][0] <= newEnd) {
            // Update new interval boundary
            newStart = Math.min(newStart, intervals[idx][0]);
            newEnd = Math.max(newEnd, intervals[idx][1]);
            idx++;
        }
        // Append new interval
        ans.add(new int[]{newStart, newEnd});

        // Append the remaining intervals
        while (idx < intervals.length) {
            ans.add(new int[]{intervals[idx][0], intervals[idx][1]});
            idx++;
        }

        // Transfer data structure before return
        return ans.toArray(new int[ans.size()][]);
    }

    public static void main(String[] args) {

        // Test case 1
        int[][] intervals1 = {{1,3},{6,9}};
        int[] newInterval1 = {2,5};
        int[][] result1 = new solution1().insert(intervals1, newInterval1);
        System.out.println(Arrays.deepToString(result1));

        // Test case 2
        int[][] intervals2 = {{1,2},{3,5},{6,7},{8,10},{12,16}};
        int[] newInterval2 = {4,8};
        int[][] result2 = new solution1().insert(intervals2, newInterval2);
        System.out.println(Arrays.deepToString(result2));

    }
}
