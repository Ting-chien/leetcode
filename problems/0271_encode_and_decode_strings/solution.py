from typing import List


class Solution:
    """
    Try to concatenate each string with length in prefix.
    
    For example,

        strs = ["hello", "world"]

        -> "5#hello5#world"

    When decode the encoded string, use two pointers i and j,
    use cursor i to find # and use j to find string according
    to the length before #.
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res


    def decode(self, s: str) -> List[str]:

        res = []
        i, j = 0, 0

        while i < len(s):

            if s[i] == "#":
                # Get the length of string
                l = int(s[j:i])
                # Get the string
                j = i + 1 + l
                res.append(s[i+1:j])
                # Update cursor i
                i = j

            i += 1

        return res
    
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
msg = Solution().encode(["Hello","World"])
print(f"msg={msg}")
data = Solution().decode(msg)
print(f"data={data}")

# Input: dummy_input = ["we","say",":","yes","!@#$%^&*()"]
# Output: ["we","say",":","yes","!@#$%^&*()"]
msg = Solution().encode(["we","say",":","yes","!@#$%^&*()"])
print(f"msg={msg}")
data = Solution().decode(msg)
print(f"data={data}")