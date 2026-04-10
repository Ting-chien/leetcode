from typing import List
from functools import cmp_to_key



class Solution1:
    def largestNumber(self, nums: List[int]) -> str:
        def mycmp(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0
        # sort the elements in ascending order
        sorted_nums = sorted([str(num) for num in nums], key=cmp_to_key(mycmp), reverse=True)
        # concatenate all elements if the first element is not "0"
        return "".join(sorted_nums) if sorted_nums[0] != "0" else "0"


class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        # write custom sort function by comparing two str
        # if x + y > y + x, then x shold be infront of y
        class cmp(str):
            def __lt__(x, y):
                return x + y > y + x
        nums = sorted([str(n) for n in nums], key=cmp)
        return "".join(nums) if nums[0] != "0" else "0"

if __name__ == "__main__":

    # Example 1:
    # Input: nums = [10,2]
    # Output: "210"
    res = Solution2().largestNumber([10, 2, 0])
    print(res)

    # Example 2:
    # Input: nums = [3,30,34,5,9]
    # Output: "9534330"
    res = Solution2().largestNumber([30,5,34,3,9])
    print(res)

    # Example 3:
    # Input: nums = [0,0]
    # Output: "0"
    res = Solution2().largestNumber([0, 0])
    print(res)