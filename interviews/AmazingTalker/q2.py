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
                # else
                elif curr_sum == max_sum:
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
    print(sol.two_sum_lessK([4, 3, 2, 1, 4, 3, 2, 1], 10))
    print(sol.two_sum_lessK([2, 1], 5))
    print(sol.two_sum_lessK([-2, -1, -1, -2], -2))
    # print (two_sum_less_than_k([1, 2, 3, 4], 4))		# [(1, 2)]
	# print (two_sum_less_than_k([1, 2, 3], 3))			# []
	# print (two_sum_less_than_k([1, 2, 2, 3, 4], 5))		# [(1, 3), (2, 2)]
	# print (two_sum_less_than_k([4, 3, 2, 1, 4, 3, 2, 1], 10))	# [(4, 4)]
	# print (two_sum_less_than_k([2, 1], 5))				# [(1, 2)]
	# print (two_sum_less_than_k([-2, -1, -1, -2], -2))	# [(-2, -1)]