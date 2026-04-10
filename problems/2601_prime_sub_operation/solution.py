from typing import List


class Solution:

    def is_prime(self, num: int) -> bool:
        """Return True if input number is prime, False for not."""
        for i in range(2, (num//2)+1):
            if num % i == 0:
                return False
        return True


    def primeSubOperation(self, nums: List[int]) -> bool:
        # Iterate through nums from highest index
        for i in range(len(nums)-2, -1, -1):
            # Perform the algorithm when nums[i+1] is not stricktly larger than nums[i]
            if nums[i] >= nums[i+1]:
                # Iterate through primes from lowest value
                p = 2
                while p < nums[i]:
                    if nums[i] - p < nums[i+1]:
                        # nums[i] -= p
                        break
                    p += 1
                    while not self.is_prime(p):
                        p += 1
                if p < nums[i]:
                    nums[i] -= p
                else:
                    return False
        return True
    


# Example 1:
# Input: nums = [4,9,6,10]
# Output: true
res = Solution().primeSubOperation(nums=[4,9,6,10])
print(res)

# Example 2:
# Input: nums = [6,8,11,12]
# Output: true
res = Solution().primeSubOperation(nums=[6,8,11,12])
print(res)

# Example 3:
# Input: nums = [5,8,3]
# Output: false
res = Solution().primeSubOperation(nums=[5,8,3])
print(res)