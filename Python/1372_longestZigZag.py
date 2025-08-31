from typing import Optional, Tuple

from utils.binary_tree import insert_level_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestPath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.longestPath(root.left), self.longestPath(root.right))

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Use BFS to choose each node in tree, and select a node and direction
        to traverse by DFS to find longest zigzag path.

        Complexity
        * Time: O(n^2) - Time Limit Exceed ❌. For BFS we will go through every nodes
        in the tree so the complexity is O(n), and for DFS's best complexity is O(logn)
        and O(n) for worst case. So total worst cast is O(n^2)
        * Space: (n) - ???. Worst case in DFS and BFS are both O(n)

        Time: 23:10
        """

        # Find longest zigzag path by DFS
        LEFT = "left"
        RIGHT = "right"
        memo = {} # Use memo to store node already visited
        def dfs(root: Optional[TreeNode], direction: str) -> int:
            if not root:
                return 0
            if not memo.get((root, direction)):
                memo[(root, direction)] = (1 + dfs(root.left, LEFT)) \
                                        if direction == RIGHT \
                                        else (1 + dfs(root.right, RIGHT))
            return memo[(root, direction)]
        
        # Go through every nodes and direction
        queue = [[root]]
        ans = 0
        while queue:
            nodes = queue.pop()
            tmp = []
            for node in nodes:
                if node.left:
                    ans = max(ans, dfs(node.left, LEFT))
                    tmp.append(node.left)
                if node.right:
                    ans = max(ans, dfs(node.right, RIGHT))
                    tmp.append(node.right)
            if tmp:
                queue.append(tmp)

        return ans
    

class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Optimize solution 1 by memorization

        Complexity
        * Time: O(n^2) - Beats 5.02%
        * Space: (n) - Beats 5.27%

        Time: 26:08
        """

        # Find longest zigzag path by DFS
        LEFT = "left"
        RIGHT = "right"
        memo = {} # Use memo to store node already visited
        def dfs(root: Optional[TreeNode], direction: str) -> int:
            if not root:
                return 0
            if not memo.get((root, direction)):
                memo[(root, direction)] = (1 + dfs(root.left, LEFT)) \
                                        if direction == RIGHT \
                                        else (1 + dfs(root.right, RIGHT))
            return memo[(root, direction)]
        
        # Go through every nodes and direction
        queue = [[root]]
        ans = 0
        while queue:
            nodes = queue.pop()
            tmp = []
            for node in nodes:
                if node.left:
                    ans = max(ans, dfs(node.left, LEFT))
                    tmp.append(node.left)
                if node.right:
                    ans = max(ans, dfs(node.right, RIGHT))
                    tmp.append(node.right)
            if tmp:
                queue.append(tmp)

        return ans
    

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        ChatGPT 建議解法，用 DFS 往下遍歷，並且同時紀錄左右 zigzag 最大長度

        Complexity
        * Time: O(n)
        * Space: O(n)
        """
        ans = 0
        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            """
            返回左、右子樹的最大深度
            """
            if not root:
                return -1, -1
            
            left = dfs(root.left)[1] + 1 # 走左邊，所以下一步要取右子樹
            right = dfs(root.right)[0] + 1 # 反之要取左子樹

            # 紀錄當前最深的 zigzag
            nonlocal ans
            ans = max(ans, left, right)

            return left, right
        
        dfs(root)
        return ans
    

# Example 1:
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
root = insert_level_order([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
res = Solution().longestZigZag(root=root)
print(res)

# Example 2:
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
root = insert_level_order([1,1,1,None,1,None,None,1,1,None,1])
res = Solution().longestZigZag(root=root)
print(res)

# Example 3:
# Input: root = [1]
# Output: 0
root = insert_level_order([1])
res = Solution().longestZigZag(root=root)
print(res)
