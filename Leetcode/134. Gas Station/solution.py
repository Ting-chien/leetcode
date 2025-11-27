from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Brutal Force (TLE)"""
        # Get the net amount of gas starting from each index
        net = [g - c for g, c in zip(gas, cost)]
        n = len(net)

        # Start from each gas
        for i in range(n):
            curr = 0 # Current amount of gas ini tank
            is_success = True # Whether the truck can complete circuit
            for j in range(n):
                cursor = (i + j) % n
                curr += net[cursor]
                # If curr < 0, it means the truck can't start from gas[i]
                if curr < 0:
                    is_success = False
                    break
            # Return if success once
            if is_success:
                return i
        
        return -1
    

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Greedy: O(n)"""
        curr = 0 # Current amount of gas in tank
        total = 0 # Total amount of gas in tank
        n = len(gas)

        # Traverse from index i
        start = 0
        for i in range(n):
            net = gas[i] - cost[i]
            curr += net
            total += net
            # Start over from i+1 once curr tank < 0
            if curr < 0:
                start = i + 1
                curr = 0

        return start if total >= 0 else -1
    

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))