class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        for char in s:
            # If char is digit, keep adding curr_num
            if char.isdigit():
                curr_num = curr_num*10 + int(char)
            # If char is '[', put curr_str and curr_num to stack
            elif char == "[":
                stack.append((curr_str, curr_num))
                curr_num = 0
                curr_str = ""
            # If char is ']', take str and num from stack to form a new substr
            elif char == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + num*curr_str
            else:
                curr_str += char
        return curr_str
    
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                # First step, pop letters until we met `[`
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                # Remove `[`
                stack.pop()
                # Count how many time we need to mutiply curr_str
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                # Add curr_num*curr_str back to stack
                stack.append(int(curr_num) * curr_str)
            else:
                stack.append(char)
        return "".join(stack)
    
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(index: int) -> tuple[str, int]:
            res = ""
            num = 0
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == "[":
                    sub_str, index = dfs(index + 1)
                    res += num * sub_str
                    num = 0  # reset after using
                elif char == "]":
                    return res, index
                else:
                    res += char
                index += 1
            return res, index
        
        decoded, _ = dfs(0)
        return decoded

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
res = Solution().decodeString(s = "3[a]2[bc]")
print(res)

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
res = Solution().decodeString(s = "3[a2[c]]")
print(res)