from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Merge two list and count the length
        count = 0
        merged_list = []
        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    num = nums2.pop(0)
                    merged_list.append(num)
                else:
                    num = nums1.pop(0)
                    merged_list.append(num)
            elif nums1:
                num = nums1.pop(0)
                merged_list.append(num)
            else:
                num = nums2.pop(0)
                merged_list.append(num)
            count += 1
    
        # Return middle value
        div, mod = divmod(count, 2)
        if mod == 0:
            return (merged_list[div] + merged_list[div-1]) / 2
        else:
            return merged_list[div]
        

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Use two pointers to find cursor in the middle place.
        """
        m, n = len(nums1), len(nums2)
        K = m + n # total length of merged list
        mid1, mid2 = (K - 1) // 2, K // 2 # Get two middle places to deal with odd and even situatioin

        i = j = 0
        curr = prev = 0
        for k in range(K):
            prev = curr 
            if (i < m) and (j >= n or nums1[i] < nums2[j]):
                # Use element in nums1
                curr = nums1[i]
                i += 1
            else:
                # Use element in nums2
                curr = nums2[j]
                j += 1
            # If curr meet mid2, return middle value
            if k == mid2:
                if K % 2 == 0:
                    return (prev + curr) / 2
                else:
                    return curr


res = Solution().findMedianSortedArrays([1,3], [2])
print(res)

res = Solution().findMedianSortedArrays([1,2], [3,4])
print(res)