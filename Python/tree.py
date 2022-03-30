class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = Node(val)
            else:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = Node(val)
        else:
            self.val = val

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.val)
            res = res + self.inorder_traversal(root.right)
        return res

    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.val)
        return res

if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    print(root.left.right)
    print(root.left.right.val)

    print(root.inorder_traversal(root))
    print(root.preorder_traversal(root))
    print(root.postorder_traversal(root))