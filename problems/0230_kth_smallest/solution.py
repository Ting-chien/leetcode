from typing import Optional
from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Intuition: Use in-order traverse to go through all nodes
        from BST. 

                A
              /   \
             B     C

            B -> A -> C

        """

        cnt = 0
        curr_max = float('-inf')

        def inorder_traverse(node: Optional[TreeNode]):
            if not node:
                return 
            # 遍歷左子樹
            inorder_traverse(node.left)
            # 比較當前節點大小
            nonlocal cnt, curr_max
            if cnt < k:
                curr_max = max(curr_max, node.val)
                cnt += 1
            # 遍歷右子樹
            inorder_traverse(node.right)

        inorder_traverse(node=root)
        return curr_max
    
# Example 1:
# Input: root = [3,1,4,None,2], k = 1
# Output: 1
root = insert_level_order([3,1,4,None,2])
res = Solution().kthSmallest(root=root, k=1)
print(res)

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
root = insert_level_order([5,3,6,2,4,None,None,1])
res = Solution().kthSmallest(root=root, k=3)
print(res)
