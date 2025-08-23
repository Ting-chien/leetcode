from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Intuition:
            
            Input: nums1, nums2
            Output: res with lenght == len(nums1)
            Target: When nums1[i] == nums2[j], find the index of next greater 
            element of nums[j] in nums2. Return -1 if not exist.

        Condition:

            1. nums1 is subset of nums2
            2. All integers in nums1 and nums2 are unique
            3. 1 <= len(nums1), len(nums2) <= 1000

        Algorithm:

            1. Use monotonic stack to get next greater element of each number
            2. Find by order of nums1

        Complexity:

            * Time: O(M+M*N)
            * Space: O(M+N)
        
        """
        M, N = len(nums1), len(nums2)
        d = {} # Store index of next greater element Space:O(N)
        stack = [] # A stack to help us find next greater element Space:O(M)

        # Find greater element of each element in nums2
        # Time=O(N) in monotonic stack
        for i in range(N):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                d[idx] = nums2[i]
            stack.append(i)

        # Find index of nums[i] in nums2 and add the index
        # of next greater element to ans
        # Time=O(M*N), find index in array is O(N)
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            ans.append(d.get(idx, -1))

        return ans
    

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Since nums1 is a subset of nums2, we can only records elements exist 
        in nums1 to prevent O(M*N) in finding nums1[i] == nums2[j]

        Complexity
        * Time: O(M+N)
        * Space: O(M)
        """
        tmp = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                res[tmp[stack.pop()]] = nums2[i]
            if nums2[i] in tmp:
                stack.append(nums2[i])

        return res


"""
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Dry run:
    stack=[2,3], d={0:3, 1:4}
    
    Stpe2:
        num=4, idx=2, ans=[-1]
        num=1, idx=0, ans=[-1,3]
        num=2, idx=3, ans=[-1,3,-1]
"""
res = Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
print(res)