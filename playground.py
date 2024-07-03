from typing import Optional, List, Any


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_nodes(arr: List[Any]) -> Optional[ListNode]:
    dummy = curr = ListNode(0)
    for ele in arr:
        curr.next = ListNode(ele)
        curr = curr.next
    return dummy.next

def print_nodes(node: Optional[ListNode]) -> List[Any]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + preorder_traverse(root.left)
        res = res + preorder_traverse(root.right)
    return res

def insert_level_order(arr: List[Any]) -> Optional[TreeNode]:
    if not arr or not arr[0]: return None
    if len(arr) <= 1: return TreeNode(arr[0])
    
    root = TreeNode(arr[0])
    i = 1
    queue = [root]

    while i < len(arr):
        curr = queue.pop(0)
        # 插入左子節點
        curr.left = TreeNode(arr[i]) if arr[i] else None
        if arr[i]:
            queue.append(curr.left)
        i += 1
        # 插入右子節點
        if i < len(arr):
            curr.right = TreeNode(arr[i]) if arr[i] else None
            if arr[i]:
                queue.append(curr.right)
        i += 1
    
    return root


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finding three num [nums[i], nums[j], nums[k]] which
        i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice: There might be duplicate number in the array,
        but no duplicate triplets is allowable.

        Solution: 透過一個 pointer 來遍歷所有 array 中的元素，並且透過 two 
        pointers 的解題方式找尋剩下 array 中的數字。
        """
        res = []
        # 將 array 由小到大排序
        nums.sort()
        for i in range(len(nums)-2):
            # 跳過與上一個相同的 num，來避免求出重複的答案
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 透過 two pointer 解出剩下的題目
            target = 0 - nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                print(j, k)
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1]: 
                        if j < k:
                            j += 1
                        else:
                            break
                    while nums[k] == nums[k+1]: 
                        if j < k:
                            k -= 1
                        else:
                            break
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return res


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))

# Example 2:
# Input: nums = [0,1,1]
# Output: []
print(Solution().threeSum(nums=[0,1,1]))

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
print(Solution().threeSum(nums=[0,0,0]))

# Example 3:
# Input: nums = [-2,0,0,2,2]
# Output: [[-2,0,2]]
print(Solution().threeSum(nums=[-2,0,0,2,2]))