import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {

    private Map<Integer, List<Integer>> graph = new HashMap<>();

    public long weightedSum(int[] parent, int[] nums) {

        // Transfer parent into a map
        for (int c = 0; c < parent.length; c++) {
            int p = parent[c];
            if (p != -1) {
                graph.computeIfAbsent(p, k -> new ArrayList<>()).add(c);
            }
        }

        // Find the height of the tree
        int height = dfs(0);

        // Get weights of the nodes
        long weightedSum = 0;
        List<List<Integer>> queue = new ArrayList<>(List.of(List.of(0, 1))); // [[node, depth]]
        while (!queue.isEmpty()) {
            List<Integer> currentNode = queue.remove(0);
            int nodeIndex = currentNode.get(0);
            int depth = currentNode.get(1);
            weightedSum += (long) nums[nodeIndex] * (height - depth + 1);
            for (int child : graph.getOrDefault(nodeIndex, new ArrayList<>())) {
                queue.add(List.of(child, depth + 1));
            }
        }

        return weightedSum;
    }

    private int dfs(int i) {
        if (graph.getOrDefault(i, new ArrayList<>()).isEmpty()) {
            return 1;
        }
        return graph.get(i).stream().mapToInt(this::dfs).max().getAsInt() + 1;
    }

    public static void main(String[] args) {

        Solution solution = new Solution();

        // Test cases 1
        System.out.println(solution.weightedSum(new int[] {-1,0,0,0,2,2}, new int[] {5,2,3,1,4,6})); // Output: 37

        // Test cases 2
        System.out.println(solution.weightedSum(new int[] {-1,0,1,2}, new int[] {1,2,3,4})); // Output: 20
    }
}