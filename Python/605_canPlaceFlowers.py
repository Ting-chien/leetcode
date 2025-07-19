from typing import List


# class Solution:
#     def get_max_plots(self, num_of_zero: int) -> int:
#         div, mod = divmod(num_of_zero, 2)
#         if mod == 1:
#             return div
#         else:
#             return div - 1
    
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         """
#         Iterate through flowerbed and count number of 0 between two 1,
#         and calculate how many new flowers can be planted in those 0s.

#         Edge case:
#         1. Would flowerbed be all zero ?
#         2. Wourd if be [0, 0] ?
#         """
#         left, right = -1, 1
#         while right < len(flowerbed) + 1:
#             if right == len(flowerbed) or flowerbed[right] == 1:
#                 num_of_zero = right - left - (0 if right == len(flowerbed) or left == -1 else 1)
#                 print(f"num_of_zero={num_of_zero}")
#                 max_plots = self.get_max_plots(num_of_zero)
#                 print(f"max_plots={max_plots}")
#                 n -= max_plots
#                 left = right
#             # Check if we plot all new flowers
#             print(f"n={n}")
#             if n <= 0:
#                 return True
#             right += 1
#         return False


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Iterate thought flowerbed, and find plantable place, and 
        check if both left and right side are zero or boundary. If
        so, we can plant a new flower
        """
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_side_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_side_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if left_side_empty and right_side_empty:
                    cnt += 1
                    flowerbed[i] = 1
        return cnt >= n
    

# # Example 1:
# # Input: flowerbed = [1,0,0,0,1], n = 1
# # Output: true
# res = Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)
# print(res)

# # Example 2:
# # Input: flowerbed = [1,0,0,0,1], n = 2
# # Output: false
# res = Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)
# print(res)

# # Example 3:
# # Input: flowerbed = [1,0,0,0,0], n = 2
# # Output: true
# res = Solution().canPlaceFlowers(flowerbed = [1,0,0,0,0], n = 2)
# print(res)

# Example 3:
# Input: flowerbed = [0,0,1,0,1], n = 1
# Output: true
res = Solution().canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1)
print(res)

