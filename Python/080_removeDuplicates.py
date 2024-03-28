from tkinter.messagebox import NO
from typing import List

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Return answer if length less than 2
        if len(nums) <= 2: return len(nums)

        # While three elements are identical in a row
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-1] == nums[i-2]:
                nums.pop(i)
            else:
                i += 1

        return i

class Solution2:
    '''
    解法貳利用快慢指針，並利用慢指針寫入，快指針做遍歷讀取
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0

        # 快指針透過遍歷掃過所有元素
        for num in nums:
            if i < 2 or num != nums[i-2]:
                # 若符合條件透過慢指針寫入
                nums[i] = num
                i += 1

        return i

class Solution3:
    '''
    解法三一樣使用快慢指針，差別是有明確訂出兩指針位置
    '''
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        
        if n <= 2: return n

        count = 1
        slow, fast = 0, 1
        while fast < n:
            if nums[slow] != nums[fast]:
                slow +=1 
                nums[slow] = nums[fast]
                count = 1
            else:
                if count < 2:
                    slow +=1 
                    nums[slow] = nums[fast]
                    count += 1
            fast += 1

        return slow + 1


if __name__ == '__main__':
    sol = Solution3()
    ans1 = sol.removeDuplicates([1,1,1,2,2,3])
    print("Ans 1 is {}".format(ans1))
    ans2 = sol.removeDuplicates([0,0,1,1,1,1,2,3,3])
    print("Ans 2 is {}".format(ans2))
    ans3 = sol.removeDuplicates([1,1,1,1])
    print("Ans 3 is {}".format(ans3))