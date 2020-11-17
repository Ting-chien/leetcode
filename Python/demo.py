class Solution:
    def removeDuplicates(self, nums):
        length = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                nums.insert(length, nums.pop(i))
                return nums[:length+1]
            if nums[i] != nums[i+1]:
                length += 1
                nums.insert(length-1, nums.pop(i))
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))