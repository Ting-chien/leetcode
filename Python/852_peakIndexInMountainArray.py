from typing import List

class Solution1:
    '''
    Linear Search
    Time complexity: O(n)
    '''
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i

class Solution2:
    '''
    Binary Search
    Time complexity: O(log n)
    '''
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid+1] > arr[mid] and arr[mid] > arr[mid-1]:
                left = mid + 1
            elif arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
                right = mid - 1
            elif arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            else:
                left = mid + 1

if __name__ == '__main__':
    sol = Solution2()
    # print(sol.peakIndexInMountainArray([0,1,0]))
    # print(sol.peakIndexInMountainArray([0,2,1,0]))
    # print(sol.peakIndexInMountainArray([0,10,5,2]))
    print(sol.peakIndexInMountainArray([3,9,8,6,4]))