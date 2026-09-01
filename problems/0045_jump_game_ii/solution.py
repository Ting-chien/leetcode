from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Intuition: Find global max index we can
        reach, and update jump times when we meet
        the current max position.
        """
        global_max = 0
        current_max = 0
        steps = 0

        for i in range(len(nums) - 1):
            # Update global max index
            global_max = max(global_max, i+nums[i])

            # If we reach current max, we can jump again
            # and set next max available position
            if i == current_max:
                steps += 1
                current_max = global_max

        return steps


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.jump(nums = [2,3,1,1,4])) # 2

    # Test cases 2
    print(solution.jump(nums = [2,3,0,1,4])) # 2
