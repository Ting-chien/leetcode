class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        """
        Intuition: Find a subarray from nums and check if it is valid.
        """

        ans = 0
        a_b = a / b

        # Use double for loop to find all subarrays
        for i in range(len(nums)):
            num_of_even = 0
            num_of_odd = 0
            for j in range(i, len(nums)):
                # Check odd or even
                if (nums[j] % 2) == 0:
                    num_of_even += 1
                else:
                    num_of_odd += 1
                # Get ratio and check valid
                if num_of_odd > 0 and (num_of_even / num_of_odd) <= a_b:
                    ans += 1
        
        return ans