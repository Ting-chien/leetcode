from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """此題希望透過 backtrack 的方式往下查找剩餘的 nums，
        並將從 nums 裡面取出的元組組成一個陣列 path，在每一次遞
        迴時傳給 res 作為一個 subset。
        """
        res = []
        def backtrack(remains: List[int], path: List[int]):
            print(f"remains={remains}, path={path}")
            if remains == [1,2,3] and len(path) > 3: raise
            nonlocal res
            # append every subset into res
            res.append(path[:])
            print(f"res={res}")
            # go through all elements in nums recursivelly
            for i in range(len(remains)):
                path.append(remains[i])
                backtrack(remains[i+1:], path)
                path.pop()
            # return if there is no element left in nums
            return
        backtrack(nums, [])
        return res        
    

def traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + traverse(root.left)
        res = res + traverse(root.right)
    return res

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(traverse(root))

# Example 1: [1,2,3]
res = Solution().subsets([1,2,3])
print(res)

# Example 2: [0]
res = Solution().subsets([0])
print(res)
