from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    透過BFS一層層去遍歷節點，並在每一層leaf layer終將null的前一個值回傳
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []
        
        # Use a stack to store all the nodes
        stack = [root, None]
        tmp = []
        res = []

        while stack:
            curr = stack.pop(0)
            if curr:
                tmp.append(curr.val)
                if curr.left: stack.append(curr.left)
                if curr.right: stack.append(curr.right)
            else:
                res.append(tmp.pop())
                tmp = []
                if stack: stack.append(None)

        return res

class Solution:
    '''
    透過遞迴的方式去將每一層做遍歷，再將每一層最後一個元素取出
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        return [x[-1] for x in res]

    def dfs(self, root: Optional[TreeNode], level: int, res: List[List[int]]):

        # Return if no node exist
        if not root: return

        # Add new list for level
        if len(res) == level: res.append([])

        # BFS
        res[level].append(root.val)
        if root.left: self.dfs(root.left, level+1, res)
        if root.right: self.dfs(root.right, level+1, res)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # 宣告一陣列來紀錄節點
        def dfs(node: Optional[TreeNode], depth: int):
            # 若節點為空，則返回
            if not node: return
            # 判斷節點深度是否大於等於答案長度
            if depth >= len(res):
                res.append(node.val)
            # 繼續往下遞迴
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return res
    

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        嘗試用 BFS 但使用例一種方式去遍歷同一層的節點 (2025/8/9)

        Complexity
        * Time: O(n) - beats 100%
        * Space: O(W), width of tree - beats 17.12%
        """
        if not root: return []

        queue = [[root]] # 將同一層的 nodes 放在一個 list 中
        res = [] # 用來存每一層最右側的節點

        while queue:
            nodes = queue.pop(0)
            res.append(nodes[-1].val)
            tmp = []
            for node in nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp: queue.append(tmp)

        return res


if __name__ == '__main__':

    # Test case1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)

    # Test case2
    root2 = TreeNode(1)
    root2.right = TreeNode(3)

    # Test case3
    root3 = None

    sol = Solution()
    print(sol.rightSideView(root=root1))
    print(sol.rightSideView(root=root2))
    print(sol.rightSideView(root=root3))