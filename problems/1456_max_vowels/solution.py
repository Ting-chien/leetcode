class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Use a window with k length to iterate through s

        Complexity:
        * Time: O(n*k)
        * Spece: O(1)
        Time Limit Exceed
        """
        vowels = set("aeiouAEIOU")
        max_num_of_vowel = 0
        for i in range(len(s)-k+1):
            num_of_vowel = sum(1 for char in s[i:i+k] if char in vowels)
            max_num_of_vowel = max(max_num_of_vowel, num_of_vowel)
        return max_num_of_vowel
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Use a window with k length to iterate through s

        Complexity:
        * Time: O(n)
        * Spece: O(1)
        """
        vowels = set("aeiouAEIOU")
        max_num_of_vowel = num_of_vowel = sum(1 for char in s[:k] if char in vowels)
        for i in range(1, len(s)-k+1):
            # Check how many vowels in new list
            if s[i-1] in vowels:
                num_of_vowel -= 1
            if s[i+k-1] in vowels:
                num_of_vowel += 1
            # Check current maximum value
            max_num_of_vowel = max(max_num_of_vowel, num_of_vowel)
        return max_num_of_vowel
    

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
res = Solution().maxVowels(s = "abciiidef", k = 3)
print(res)

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
res = Solution().maxVowels(s = "aeiou", k = 2)
print(res)