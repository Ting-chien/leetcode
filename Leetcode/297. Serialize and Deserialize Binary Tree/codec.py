from typing import Optional
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        q = deque([root])
        nodes = [root.val]
        while q:
            node: TreeNode = q.popleft()
            nodes.append(node.left.val if node.left else None)
            nodes.append(node.right.val if node.right else None)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ",".join([str(n) for n in nodes])
        

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not nodes:
            return 
        
        # Transfer string into list
        nodes = deque(data.split(","))
        
        # Construct a tree 
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        while q:
            tmp = q.popleft()
            left = nodes.popleft()
            if left != "None":
                node = TreeNode(x=int(left))
                tmp.left = node
                q.append(node)
            right = nodes.popleft()
            if right != "None":
                node = TreeNode(x=int(right))
                tmp.right = node
                q.append(node)

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# root = TreeNode(x=1)
# root.left = TreeNode(x=2)
# root.right = TreeNode(x=3)
# root.right.left = TreeNode(x=4)
# root.right.right = TreeNode(x=5)
# ser = Codec()
# print(ser.serialize(root=root))

root = None
ser = Codec()
print(ser.serialize(root=root))