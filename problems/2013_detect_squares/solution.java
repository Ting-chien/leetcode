import java.util.HashMap;
import java.util.Map;

class Solution {

    private Map<String, Integer> counter;

    public Solution() {
        counter = new HashMap<>();
    }
    
    public void add(int[] point) {
        String key = point[0] + "#" + point[1];
        counter.put(key, counter.getOrDefault(key, 0) + 1);
    }
    
    public int count(int[] point) {
        int x1 = point[0], y1 = point[1];
        int cnt = 0;
        for (String key : counter.keySet()) {
            String[] slices = key.split("#");
            int x2 = Integer.parseInt(slices[0]);
            int y2 = Integer.parseInt(slices[1]);
            if (x1 != x2 && y1 != y2 && Math.abs(x1 - x2) == Math.abs(y1 - y2)) {
                String key1 = x1 + "#" + y2;
                String Key2 = x2 + "#" + y1;
                int c1 = counter.getOrDefault(key, 0);
                int c2 = counter.getOrDefault(key1, 0);
                int c3 = counter.getOrDefault(Key2, 0);
                cnt += c1 * c2 * c3;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Solution ds = new Solution();

        System.out.println("null"); // DetectSquares

        ds.add(new int[]{3, 10});
        System.out.println("null");

        ds.add(new int[]{11, 2});
        System.out.println("null");

        ds.add(new int[]{3, 2});
        System.out.println("null");

        System.out.println(ds.count(new int[]{11, 10})); // 1
        System.out.println(ds.count(new int[]{14, 8}));  // 0

        ds.add(new int[]{11, 2});
        System.out.println("null");

        System.out.println(ds.count(new int[]{11, 10})); // 2

    }
}
