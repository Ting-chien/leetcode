from typing import Optional

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        三種寫BFS的方法之一
        """
        res = []
        queue = [root]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if left := node.left:
                    queue.append(left)
                if right := node.right:
                    queue.append(right)
            res.append(sum(tmp))
        return res.index(max(res)) + 1
    
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        三種寫BFS的方法之二

        Complexity
        * Time: O(n) - beats 11.78%
        * Space: O(n) - beats 44.09%
        """
        res = []
        tmp = []
        queue = [root, None] # 用 None 作為每一層的分割點
        while queue:
            node = queue.pop(0)
            if node:
                tmp.append(node.val)
                if left := node.left:
                    queue.append(left)
                if right := node.right:
                    queue.append(right)
            else:
                res.append(sum(tmp))
                tmp = []
                if queue: queue.append(None)
        return res.index(max(res)) + 1

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        三種寫BFS的方法之三

        Complexity
        * Time: O(n) - beats 79.89%
        * Space: O(n) - beats 77.05%
        """
        res = []
        queue = [[root]] # 將同一層的節點放在一起
        while queue:
            nodes = queue.pop(0)
            tmp = []
            sum = 0
            for node in nodes:
                sum += node.val
                if left := node.left:
                    tmp.append(left)
                if right := node.right:
                    tmp.append(right)
            res.append(sum)
            if tmp: queue.append(tmp)
        return res.index(max(res)) + 1

# Example 1:
# Input: [1,7,0,7,-8,null,null]
# Output: 2
res = Solution().maxLevelSum(insert_level_order([1,7,0,7,-8,None,None]))
print(res)