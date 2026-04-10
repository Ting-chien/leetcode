from typing import Optional

from utils.binary_tree import insert_level_order, preorder_traverse


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        1. 透過 bfs 將每一層的節點加總
        2. 再次遍歷該層的每一節點，並將新的值給予左、右子節點
        """
        root.val = 0
        q = [root]
        while q:
            copy_q = q.copy()
            q = []
            # 遍歷該層的所有節點，並計算子節點的總和
            nxt_levle_sum = 0
            for node in copy_q:
                if left := node.left:
                    q.append(left)
                    nxt_levle_sum += left.val
                if right := node.right:
                    q.append(right)
                    nxt_levle_sum += right.val
            # 再次遍歷該層所有的節點，並計算各自子節點的值
            # 計算方式為 nxt_level_sum - children_sum
            for node in copy_q:
                children_sum = (node.left.val if node.left else 0) \
                            + (node.right.val if node.right else 0)
                if node.left: node.left.val = nxt_levle_sum - children_sum
                if node.right: node.right.val = nxt_levle_sum - children_sum
        return root
    


# Example 3
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
root = insert_level_order([5,4,9,1,10,None,7])
res = Solution().replaceValueInTree(root=root)
print(preorder_traverse(res))

# Example 3
# Input: root = [3,1,2]
# Output: [0,0,0]
root = insert_level_order([3,1,2])
res = Solution().replaceValueInTree(root=root)
print(preorder_traverse(res))