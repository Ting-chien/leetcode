from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Failed: Array 中的順序有被打亂過，因次用單純的二元
    分類搜尋會往錯的方向找。像是 Test1，明明 target 在
    nums 的右側，但因為 target < nums[3] 所以被判定為
    target 在 nums 左側。
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

def search(nums: List[int], target: int) -> int:


if __name__ == '__main__':

    # Test 1
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))

    # Test 2
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(search(nums, target))

    # Test 3
    nums = [1]
    target = 0
    print(search(nums, target))