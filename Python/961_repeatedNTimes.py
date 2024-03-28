from this import d
from typing import List

class Solution1:
    '''
    This solution come with the idea of making a array with
    the length of len(nums)/2+1. Hence, if any index with value
    over 1, return the answer.
    '''
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        # Make a list with l=len(nums)/2+1
        d = {}

        # Count the numbers in nums
        for num in nums:
            if num in d:
                return num
            else:
                d[num] = True

class Solution2:
    '''
    This solution come with the idea of making a array with
    the length of len(nums)/2+1. Hence, if any index with value
    over 1, return the answer.
    '''
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        s = set()

        # Count the numbers in nums
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)

if __name__ == '__main__':
    sol = Solution2()
    ans1 = sol.repeatedNTimes([1,2,3,3])
    print("Ans 1 is {}".format(ans1))
    ans2 = sol.repeatedNTimes([2,1,2,5,3,2])
    print("Ans 2 is {}".format(ans2))
    ans3 = sol.repeatedNTimes([5,1,5,2,5,3,5,4])
    print("Ans 3 is {}".format(ans3))