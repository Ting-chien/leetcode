from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Methods
        1. 透過 queue 來遍歷整棵樹
        2. 每次遍歷一層時，將該層的最大值加入 res
        3. 最後回傳 res
        """
        queue = [root]
        res = []
        while queue:
            tmp = []
            # 找到該層最大的node值
            res.append(max(node.val for node in queue))
            # 將下一層的 node 加入 queue
            while queue:
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue += tmp
        return res
