# class MaxArea:

#     def solution1(self, height):

#         max_area = 0

#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 area = (j - i) * min(height[i], height[j])
#                 max_area = max(max_area, area)

#         return max_area

#     def solution2(self, height):

#         lhs_pointer = 0
#         rhs_pointer = len(height) - 1

#         max_area = 0
#         minimize = lambda m,n: m if m > n else n

#         while lhs_pointer < rhs_pointer:
#             area = (rhs_pointer - lhs_pointer) * min(height[lhs_pointer], height[rhs_pointer])
#             max_area = max(max_area, area)
#             if height[lhs_pointer] > height[rhs_pointer]:
#                 rhs_pointer -= 1
#             else:
#                 lhs_pointer += 1

#         return max_area

# if __name__ == "__main__":
#     question = MaxArea()
#     print(question.solution2([1,8,6,2,5,4,8,3,7]))


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers
         * time complexity: O(n)
         * space complexity: O(1)
        """
        # Initialize start pointers and max_area
        l_p, r_p = 0, len(height)-1
        max_area = float("-inf")

        # iterate left and right pointer
        while l_p < r_p:
            # compare current area and max area
            l_height = height[l_p]
            r_height = height[r_p]
            area = min(l_height, r_height) * (r_p-l_p)
            max_area = max(max_area, area)
            if l_height < r_height:
                l_p += 1
            else:
                r_p -= 1

        return max_area
    

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))