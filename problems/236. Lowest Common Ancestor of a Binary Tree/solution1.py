class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Terminate the recursion when we found p or q, or when the root is empty
        if not root or root == p or root == q:
            return root
        
        # Dive into left and right tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Once the p and q exist in different side of tree
        if left and right:
            # LCA will be the intersection
            return root
        # Or p and q in the same side
        else:
            # LCA will be p or q
            return left or right


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # Test case 1, p=5 and q=1, LCA=3
    sol = Solution()
    print(sol.lowestCommonAncestor(root, root.left, root.right))

    # Test case 2, p=5 and q=4, LCA=5
    sol = Solution()
    print(sol.lowestCommonAncestor(root, root.left, root.left.right.right))