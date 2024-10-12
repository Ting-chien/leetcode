from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        # Use queue to traverse and a flag to tell when to save values in the same order
        res = [[root.val]]
        queue = [root, None]

        while queue and queue != [None]:
            curr = queue.pop(0)
            if curr:
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            else:
                tmp = []
                for node in queue:
                    tmp.append(node.val)
                res.append(tmp)
                queue.append(None)
            # print(res)
        return res

class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''Use recursion to implement BFS'''
        if not root: return []
        res = []

        def bfs(node: Optional[TreeNode], level: int) -> None:

            if not node: return

            nonlocal res
            if len(res) > level and res[level]:
                res[level].append(node.val)
            else:
                res.append([node.val])

            bfs(node.left, level+1)
            bfs(node.right, level+1)

        bfs(root, 0)
        return res
    

class Solution3:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [root]
        value = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if left := node.left:
                    queue.append(left)
                if right := node.right:
                    queue.append(right)
            value.append(tmp)
        return value
        

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution3()
    print(sol.levelOrder(root=root))