from typing import List


class Solution:

    def two_sum_lessK(self, A: List[int], K: int):

        # Sort the array
        A.sort()

        # Iterate with two pointer
        left = 0
        right = len(A) - 1
        max_sum = float('-inf')
        res = []
        while left < right:
            curr_sum = A[left] + A[right]
            if curr_sum < K:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    res = [[A[left],A[right]]]
                else:
                    res.append([A[left],A[right]])
                left += 1
            else:
                right -= 1
        
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.two_sum_lessK([1, 2, 3, 4], 4))
    print(sol.two_sum_lessK([1, 2, 3], 3))
    print(sol.two_sum_lessK([1, 2, 2, 3, 4], 5))