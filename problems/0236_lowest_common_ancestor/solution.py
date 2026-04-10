class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Iterate all nodes with DFS
        stack = [root]
        parents = {root: None}
        while stack:
            curr = stack.pop()
            if curr.right:
                parents[curr.right] = curr
                stack.append(curr.right)
            if curr.left:
                parents[curr.left] = curr
                stack.append(curr.left)

        # for k, v in parents.items():
        #     print("{} -> {}".format(k, v if v else None))

        # return

        # Find path of p's ancestor
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents.get(p)

        # Check if q exist in p's ancestor
        while q not in ancestors:
            q = parents.get(q)

        return q

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Condition one: find no matching result
        if not root: return None

        # Condition two: find root equals q or p
        if root == p or root == q: return root

        # Iterate left/right branch
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Compare where the LCA appears
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        

class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return if the node is empty
        if not root: return
        # check if current node is p or q
        if root.val == q.val or root.val == p.val:
            return root
        # check if p or q exist in sub tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = p_node = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = q_node = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    sol = Solution2()
    print(sol.lowestCommonAncestor(root=root, p=p_node, q=q_node).val)