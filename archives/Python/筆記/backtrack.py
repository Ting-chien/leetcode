from typing import List


result = []

def backtrack(nums: List[int], arr: List[int]):
    """
    Condition1. 排列組合，可重複使用列表中的元素
    """
    if len(arr) == len(nums):
        result.append(arr[:])
        return
    for i in range(len(nums)):
        arr.append(nums[i])
        backtrack(nums, arr)
        arr.pop()

backtrack(nums=[1, 2, 3], arr=[])
print(result)


##################################################

result = []

def backtrack(nums: List[int], arr: List[int]):
    """
    Condiftion2. 排列組合，不可重複使用列表中的元素
    """
    if len(nums) == 0:
        result.append(arr[:])
        return
    for i in range(len(nums)):
        arr.append(nums[i])
        # 要移除已使用過的元素
        remains = nums[:]
        remains.remove(nums[i])
        backtrack(remains, arr)
        arr.pop()

backtrack(nums=[1, 2, 3], arr=[])
print(result)


##################################################

result = []

def backtrack(nums: List[int], arr: List[int]):
    """
    排列組合，不可重複使用列表中的元素，且數組中有重複出現的數字
    """
    if len(nums) == 0:
        result.append(arr[:])
        return
    for i in range(len(nums)):
        # 掠過相同的元素
        if i > 0 and nums[i] == nums[i-1]:
            continue
        arr.append(nums[i])
        remains = nums[:]
        remains.remove(nums[i])
        backtrack(remains, arr)
        arr.pop()

backtrack(nums=[1, 1, 3], arr=[])
print(result)

##################################################

result = []

def backtrack(nums: List[int], arr: List[int], start: int):
    """
    求子集合
    """
    result.append(arr[:])
    for i in range(start, len(nums)):
        arr.append(nums[i])
        backtrack(nums, arr, i+1)
        arr.pop()

backtrack(nums=[1, 2, 3], arr=[], start=0)
print(result)

##################################################

result = []

def backtrack(nums: List[int], arr: List[int]):
    """
    求子集合，且數組中包含重複數字
    """
    result.append(arr[:])
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        arr.append(nums[i])
        backtrack(nums[i+1:], arr)
        arr.pop()

backtrack(nums=[1, 1, 3], arr=[])
print(result)