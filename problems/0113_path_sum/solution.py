from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
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

class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """使用 stack 解決問題，在 stack 中同時儲存 (node, path, curr_sum)"""
        if not root: return 
        res = []
        stack = [(root, [root.val], root.val)]
        while stack:
            node, path, tmp = stack.pop()
            if not node.left and not node.right and tmp == targetSum:
                res.append(path[:])
            if left := node.left:
                stack.append((left, path+[left.val], tmp+left.val))
            if right := node.right:
                stack.append((right, path+[right.val], tmp+right.val))
        return res


if __name__ == '__main__':
    pass