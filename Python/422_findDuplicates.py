from typing import List

class Solution1:
    '''
    Solution 1 comes with the idea of making a dictionary with
    the size of len(nums). By putting the numbers into the dictionary,
    we can know how many times the number is count.
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:

        length = len(nums)

        # Buil a dictionary with size of len(nums)  
        d = {}
        for i in range(length):
            d[i+1] = None

        # Put all numbers into the dictionary
        for num in nums:
            if not d[num]:
                d[num] = 1
            else:
                d[num] += 1

        # Check if any number appears two times
        result = []
        for k, v in d.items():
            if v == 2:
                result.append(k)

        return result

class Solution2:
    '''
    Solution 2 comes with the idea of comparing each number
    in the sorted array. If the two following numbers are the
    same, then push the number into return list.
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # Sort the list
        nums.sort()

        # Compare the two following numbers
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                result.append(nums[i])

        return result

class Solution3:
    '''
    Solution 3 is similar to solution 1. Yet, we don't declare a fix 
    size to a dictionary, we use a allocate dictionary directly.
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:

        d = {}
        result = []
        for num in nums:
            if num in d:
                result.append(num)
            else:
                d[num] = True

        return result


if __name__ == '__main__':
    sol = Solution3()
    result = sol.findDuplicates([4,3,2,7,8,2,3,1])
    print(result)