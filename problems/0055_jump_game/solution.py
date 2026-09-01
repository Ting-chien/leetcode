from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Intuition: Use Greedy to find the current max index
        can reached. Update until the value exceed nums and return
        True. Otherwise, retur False if we meet an index out
        of max reachable position.
        """
        max_idx = 0
        for i, num in enumerate(nums):
            # Return if running out of reachable position
            if i > max_idx:
                return False

            # Update current max
            max_idx = max(max_idx, i+num)

            # Early return when max_idx exceed 
            if max_idx >= len(nums):
                return True

        return True


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.canJump(nums = [2,3,1,1,4])) # True

    # Test cases 2
    print(solution.canJump(nums = [3,2,1,0,4])) # False
