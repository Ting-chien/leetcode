from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach: Use monotonic decrease stack to find next greater element.

        1. For loop nums2 with value
        2. If current value is larger than the last element in stack, pop out and store
        the two elements to a dict
        3. store the current element to stack
        4. Return a list of next greater element by find element in dict
        """
        next_g = {} # Dict to store next greater element
        stack = [] # A monotonic decrease stack

        # Find all next greater elements in nums2
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_g[prev] = num
            stack.append(num)

        # Return next greater elements 
        return [next_g.get(num, -1) for num in nums1]
