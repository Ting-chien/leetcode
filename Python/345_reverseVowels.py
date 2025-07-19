class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Iterate through s with two pointers, and switch two
        vowels by the index of pointers
        """
        left, right = 0, len(s)-1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        l = list(s)
        while left < right:
            while l[left] not in vowels:
                if left < right:
                    left += 1
                else:
                    print("Left break")
                    break
            while l[right] not in vowels:
                if left < right:
                    right -= 1
                else:
                    print("Right break")
                    break
            print(f"left={left}, right={right}")
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return "".join(l)

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
res = Solution().reverseVowels(s = "IceCreAm")
print(res)

# Example 1:
# Input: s = "mnpqrstu"
# Output: "AceCreIm"
res = Solution().reverseVowels(s = "mnpqrstu")
print(res)

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
res = Solution().reverseVowels(s = "leetcode")
print(res)
