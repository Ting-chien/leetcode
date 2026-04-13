from tools.binary_tree import insert_level_order, print_tree_level_order, find_node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Recursive"""
        # Return root if it's value is null, left or right
        if not root or root == p or root == q:
            return root

        # Traverse left and right nodes if not found,
        # try to find LCA in left and right subtrees.
        left = self.lowestCommonAncestor(root=root.left, p=p, q=q)
        right = self.lowestCommonAncestor(root=root.right, p=p, q=q)

        # If left and right both exist, root is their LCA
        # Otherwise, LCA should be one of them.
        if left and right:
            return root
        else:
            return left or right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Use stack"""

        # Record node's parent
        stack = [root]
        parents = {}
        while stack:
            node = stack.pop()
            if (left := node.left):
                stack.append(left)
                parents[left] = node
            if (right := node.right):
                stack.append(right)
                parents[right] = node

        # Find ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents.get(p)

        # Find q in p's ancestors
        while q not in ancestors:
            q = parents.get(q)

        return q


# Example 1
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
root = insert_level_order([6,2,8,0,4,7,9,None,None,3,5])
p = find_node(root, 2)
q = find_node(root, 8)
res = Solution().lowestCommonAncestor(root=root, p=p, q=q)
print_tree_level_order(res)

# Example 2
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
root = insert_level_order([6,2,8,0,4,7,9,None,None,3,5])
p = find_node(root, 2)
q = find_node(root, 4)
res = Solution().lowestCommonAncestor(root=root, p=p, q=q)
print_tree_level_order(res)