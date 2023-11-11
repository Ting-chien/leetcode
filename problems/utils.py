from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"ListNoe(val={self.val})"
    def add(self, curNode, addNode):
        addNode.next = curNode
        curNode = addNode
        return curNode

def print_linked_list(head):
    while head:
        print(head.val, end="")
        head = head.next
        if head: print("=>", end="")

def pretty_print(res: Optional[ListNode]):
    while res != None:
        if res.next == None:
            print(res.val)
        else:
            print(res.val, "->", end=" ")
        res = res.next