from operator import le
from turtle import right
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True

        if p and q:
            if (self.isSameTree(p.left, q.left) and
                p.val == q.val and
                self.isSameTree(p.right, q.right)):
                return True

        return False

class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = []
        stack_q = []
        curr_p, curr_q = p, q
        while stack_p or stack_q or curr_p or curr_q:
            while curr_p or curr_q:
                if curr_p:
                    print("curr_p is {}".format(curr_p.val))
                    stack_p.append(curr_p)
                    curr_p = curr_p.left
                if curr_q:
                    print("curr_q is {}".format(curr_q.val))
                    stack_q.append(curr_q)
                    curr_q = curr_q.left
            print(stack_p)
            print(stack_q)
            if not stack_p or not stack_q or len(stack_p) != len(stack_q): 
                return False
            else:
                curr_p = stack_p.pop()
                curr_q = stack_q.pop()
                if curr_p.val != curr_q.val: return False
                curr_p = curr_p.right
                curr_q = curr_q.right

        return True

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # 助教解法
    stackP = []
    stackQ = []
    stackP.append(p)
    stackQ.append(q)
    while stackP and stackQ:
        curP = stackP.pop()
        curQ = stackQ.pop()
        if not curP and not curQ:
            continue
        if not curP or not curQ:
            return False
        if curP.val != curQ.val:
            return False
        stackP.append(curP.right)
        stackP.append(curP.left)
        stackQ.append(curQ.right)
        stackQ.append(curQ.left)
            
    return not stackP and not stackQ


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(3)
    q.right = TreeNode(2)
    sol = Solution2()
    print(sol.isSameTree(None, TreeNode(0)))