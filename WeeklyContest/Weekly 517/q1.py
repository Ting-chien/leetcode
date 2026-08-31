class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        """
        Intuition: Iterate through nums, add 1 to counter once
        find a new letter, minus 1 to counter once visit again
        in different block.

        Complexity
        - Time: O(n)
        - Space: O(1)
        """

        special = {nums[0]: True}
        
        for i in range(1, len(nums)):
            
            # Same letter in a block
            if nums[i] == nums[i-1]:
                continue

            # Change blocks
            num = nums[i]
            if num in special:
                # Not special when num appear in another block
                special[num] = False
            else:
                # A new num appears
                special[num] = True

        return sum(1 for val in special.values() if val)


if __name__ == "__main__":

    sol = Solution()

    # Test case 1
    print(sol.countSpecialIntegers(nums = [1,2,2,1])) # Expected output: 1

    # Test case 2
    print(sol.countSpecialIntegers(nums = [3,3,1,2,2,1])) # Expected output: 2


    