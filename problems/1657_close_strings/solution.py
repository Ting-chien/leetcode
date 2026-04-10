class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Check length
        if len(word1) != len(word2):
            return False
        
        # Check if occurence of letters in word1 and word2 are the same
        s1, s2 = set(word1), set(word2)
        if s1 != s2:
            return False
        
        # Calculate occurence times
        counter1, counter2 = {}, {}
        for char1, char2 in zip(word1, word2):
            counter1[char1] = counter1.get(char1, 0) + 1
            counter2[char2] = counter2.get(char2, 0) + 1

        # Check if occurence time are the same
        occurence1 = list(counter1.values())
        occurence2 = list(counter2.values())
        if sorted(occurence1) != sorted(occurence2):
            return False
        
        return True
    

# Example 1:
# Input: word1="aaabbbbccddeeeeefffff", word2="aaaaabbcccdddeeeeffff"
# Output: False
res = Solution().closeStrings(word1="aaabbbbccddeeeeefffff", word2="aaaaabbcccdddeeeeffff")
print(res)