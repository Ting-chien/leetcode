from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        # Step 1. 在 preorder 中找到根節點
        root = TreeNode(preorder[0])

        # Step 2. 在 inorder 中根據根節點位置找出左右子樹的分佈
        idx = inorder.index(preorder[0])

        # Step 3. 藉由遞迴反覆執行以上操作
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root