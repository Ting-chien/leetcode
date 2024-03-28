from typing import List

class Solution1:
    '''
    Naive idea, using dictionary to save every numbers
    appear in the list. Save the number to the result if
    it is already exist.
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Declare a dictionary
        d = {}
        for num in nums:
            if num in d:
                return num
            else:
                d[num] = True

class Solution2:
    '''
    The problem says it has n numbers and the numbers appear
    between 1~(n-1).
    '''
    def findDuplicate(self, nums: List[int]) -> int:

        start, end = 0, len(nums)-1

        while start+1 < end:

            mid = (start+end) // 2
            
            count = 0
            for num in nums:
                if num > mid and num <= end:
                    count += 1
            print(f'mid={mid}, count={count}')
            if count > end - mid:
                start = mid
            else:
                end = mid

        return end

        
if __name__ == '__main__':
    sol = Solution2()
    ans1 = sol.findDuplicate([1,3,4,2,2])
    print(ans1)
    ans2 = sol.findDuplicate([3,1,3,4,2])
    print(ans2)