import heapq
from typing import List, Tuple

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Use a queue with length equal to k to store first k large
        elements from nums.

        If nums=[3,2,1,5,6,4], k=2

            queue=[float('-inf'), float('-inf')]

            num=3, queue=[3,float('-inf')]
            num=2, queue=[3,2]
            num=1, queue=[3,2]
            num=5, queue=[5,3]
            num=6, queue=[6,5]
            num=4, queue=[6,5]

        Approach
        1. Iterate nums from index=0, nums[i]
        2. Pop first element from queue queue[0] and compare with nums[i],
        put the bigger one into queue and use the smaller one as next reference
        3. Repeat k times

        Complexity
        * Time: O(n*k) - Time Limit Exceeded
        * Space: O(k)
        """
        queue = [float('-inf')] * k
        for num in nums:
            num1 = num
            for _ in range(k):
                num2 = queue.pop(0)
                bigger, smaller = self.get_bigger_and_smaller(num1, num2)
                queue.append(bigger)
                num1 = smaller
        return queue[-1]

    def get_bigger_and_smaller(self, num1: int, num2: int) -> Tuple[int, int]:
        return (num1, num2) if num1 > num2 else (num2, num1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Try to use min heap instead maintain a queue manually

        Complexity
        * Time: O(nlogn) - beats 86.72%
        * Space: O(k) - beats 69.88%
        """
        min_h = nums[:k]
        heapq.heapify(min_h)
        for num in nums:
            if num > min_h[0]:
                heapq.heappop(min_h) # O(logN)
                heapq.heappush(min_h, num) # O(logN)
        return min_h[0]

    
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
res = Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2)
print(res)

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
res = Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)
print(res)