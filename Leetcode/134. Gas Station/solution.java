class Solution {
    public int canCompleteCircuit_1(int[] gas, int[] cost) {
        int n = gas.length;

        for (int start = 0; start < n; start++) {
            int tank = 0;
            int count = 0;

            while (count < n) {
                int i = (start + count) % n;
                tank += gas[i] - cost[i];

                if (tank < 0) {
                    break;  // start 不可行
                }
                count++;
            }

            if (count == n) {
                return start;  // 成功繞一圈
            }
        }

        return -1;
    }

    public int canCompleteCircuit_2(int[] gas, int[] cost) {

        // Start index for car
        int start = 0;
        // Current amount of gas in tank
        int tank = 0;
        // Total amount of gas in tank
        int total = 0;

        // Travel through gas stations
        int n = gas.length;
        for (int i=0; i<n; i++) {
            int remain = gas[i] - cost[i];
            tank += remain;
            total += remain;
            // Skip index from start~i if tank < 0
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }

        return total >= 0 ? start : -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[] gas = {1, 2, 3, 4, 5};
        int[] cost = {3, 4, 5, 1, 2};

        int result = s.canCompleteCircuit_1(gas, cost);
        System.out.println("Result: " + result);
    }
}