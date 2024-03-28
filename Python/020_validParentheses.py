'''
Given a string containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.An input string 
is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Related topics: String, Stack

Similar questions: Generate Parentheses, Longest Valid Parentheses, Remove Invalid Parentheses
'''
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def isEmpty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, parentheses):
        s = Stack()
        index = 0
        balance = True
        while index < len(parentheses) and balance:
            symbol = parentheses[index]
            if symbol in "({[":
                s.push(symbol)
            else:
                if s.isEmpty():
                    balance = False
                else:
                    top = s.pop()
                    if not self.compare(top, symbol):
                        balance = False
            index += 1

        if balance and s.isEmpty():
            return True
        else:
            return False

    def compare(self, open, close):
        open_parenthese = "{[("
        close_parenthese = "}])"
        return open_parenthese.index(open) == close_parenthese.index(close)

    def isValid2(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

if __name__ == '__main__':
    example1 = "["
    example2 = "(]]"
    sol = Solution()
    print(sol.isValid(example1))
    print(sol.isValid(example2))