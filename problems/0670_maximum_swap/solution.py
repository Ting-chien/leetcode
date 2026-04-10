class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = float('-inf')
        digits = [d for d in str(num)]
        n = len(digits)
        for i in range(n):
            for j in range(i, n):
                copy_digits = digits[:] # copy a list of digits
                copy_digits[i], copy_digits[j] = copy_digits[j], copy_digits[i] # swap two digits
                max_num = max(max_num, int("".join(copy_digits))) # compare the current number with max number
        return max_num
    

# Example 1:
# Input: num = 2736
# Output: 7236
res = Solution().maximumSwap(num=2736)
print(res)

# Example 2:
# Input: num = 9973
# Output: 9973
res = Solution().maximumSwap(num=9973)
print(res)