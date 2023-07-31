from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the non-order list
        nums.sort()
        # Iterate the elements in list as target
        res = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                target = 0 - nums[i]
                lhs_pointer = i + 1
                rhs_pointer = len(nums) - 1
                while lhs_pointer < rhs_pointer:
                    if nums[lhs_pointer] + nums[rhs_pointer] == target:
                        res.append([nums[i], nums[lhs_pointer], nums[rhs_pointer]])
                        lhs_pointer += 1
                        rhs_pointer -= 1
                        # Prevent using the same value element
                        while nums[lhs_pointer] == nums[lhs_pointer-1]:
                            if lhs_pointer < rhs_pointer:
                                lhs_pointer += 1
                            else:
                                break
                        while nums[rhs_pointer] == nums[rhs_pointer+1]:
                            if lhs_pointer < rhs_pointer:
                                rhs_pointer -= 1
                            else:
                                break
                    elif nums[lhs_pointer] + nums[rhs_pointer] > target:
                        rhs_pointer -= 1
                    else:
                        lhs_pointer += 1

        return res
    

if __name__ == '__main__':

    sol = Solution()

    # Test 1
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))

    # Test 2
    nums = [0,1,1]
    print(sol.threeSum(nums))

    # Test 3
    nums = [0,0,0]
    print(sol.threeSum(nums))