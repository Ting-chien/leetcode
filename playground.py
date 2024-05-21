from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """此題應該很類似題 257. Binary Tree Paths 的概念，不過是
        要在 leaf node 檢查是否加總為 targetSum，並且 path 為一陣列而不是 str。
        若沒有符合條件則需回傳空陣列。
        """
        res = []
        def backtrack(node: Optional[TreeNode], path: List[int]):
            nonlocal res
            # return case (leaf node and sum(path) == targetSum)
            if (not node.left
                and not node.right
                and sum(path) == targetSum
            ):
                res.append(path[:])
                return
            # general case
            if left := node.left:
                backtrack(left, path + [left.val])
            if right := node.right:
                backtrack(right, path + [right.val])
        backtrack(root, [root.val])
        return res
    

def traverse(root: Optional[TreeNode]) -> List[Any]:
    """Traverse tree nodes in pre-order way."""
    res = []
    if root:
        res.append(root.val)
        res = res + traverse(root.left)
        res = res + traverse(root.right)
    return res


# Example 1: [1,2,3], targetSum=5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
res = Solution().pathSum(root, targetSum=5)
print(res)

# Example 2: [1,2], targetSum=0
root = TreeNode(1)
root.left = TreeNode(2)
res = Solution().pathSum(root, targetSum=0)
print(res)
