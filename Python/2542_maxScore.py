import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Use DFS to find all combination of index with length k, and calculate
        all possible product of sum(nums1[C(n,k)]) * min(nums2[C(n,k)]).

        Complexity - Time Limit Exceed ❌
        * Time: O(C(n,k)*k) - C(n,k) combination with O(k) for sum and min each time
        * Space: O(C(n,k)*k) - There are C(n,k) results with length k
        """
        N = len(nums1)
        combinations = []
        def dfs(start: int, comb: List[int]):
            if len(comb) == k:
                combinations.append(comb)
                return
            for i in range(start, N):
                dfs(i+1, comb+[i])
        dfs(0, [])
        
        max_val = 0
        for comb in combinations:
            sub_nums1 = [nums1[idx] for idx in comb]
            sub_nums2 = [nums2[idx] for idx in comb]
            curr_val = sum(sub_nums1) * min(sub_nums2)
            max_val = max(max_val, curr_val)
        
        return max_val
    

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        We can use a heap with length k to maintain the maximum sum of 
        nums1, and iterate from the smallest number of nums2

        Complexity
        * Time: O(nlogn) - 83.38% O(nlogn) in sorting and O(nlogk) in heap push/pop
        * Space: O(k)
        """
        # Sort by nums2 in descending order
        pairs = sorted(zip(nums2, nums1), reverse=True)

        # Use some variables to keep heap's information
        heap = []
        total = 0
        ans = 0
        for n2, n1 in pairs:
            # Remove min num in nums1 if heap is already full
            if len(heap) == k:
                total -= heapq.heappop(heap)
            # Add new number in heap
            heapq.heappush(heap, n1)
            total += n1
            # Count max
            if len(heap) == k:
                ans = max(ans, total*n2)
        return ans


# Example 1:
# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
res = Solution().maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3)
print(res)

# Example 2:
# Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
# Output: 30
res = Solution().maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1)
print(res)