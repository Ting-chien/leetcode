class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Complexity
         - Time: O(n^3)
         - Space: O(n)
        """
        
        cur_len, max_len = 0, 0
        sub = ""
        slow, fast = 0, 0
        n = len(s)

        while fast < n:

            sub = s[slow:fast+1]
            # Step 1. Add character count
            counter = {}
            for char in sub:
                counter[char] = counter.get(char, 0) + 1

            # Check if substring valid
            if all([v < 2 for v in counter.values()]):
                max_len = max(max_len, len(sub))
                fast += 1
                continue

            # If invalid, remove from slow pointer
            while slow < fast:
                char = s[slow]
                counter[char] = counter.get(char) - 1
                slow += 1
                if all([v < 2 for v in counter.values()]):
                    break

        return max_len
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Complexity
         - Time: O(n^2), n is the length of s
         - Space: O(min(26,m)), m is the difference of chracters in s
        """

        cur_len = 0 # Length of current substring
        max_len = 0 # Maximum length of substring
        counter = {} # Count appearance of characters
        slow, fast = 0, 0 # Two pointers to locate substring
        n = len(s)

        while fast < n:

            # Update counter
            char = s[fast]
            counter[char] = counter.get(char, 0) + 1
            cur_len += 1

            # Check if substring valid
            if all([val < 2 for val in counter.values()]):
                max_len = max(max_len, cur_len)
            else:
                while slow < fast:
                    char = s[slow]
                    counter[char] = counter.get(char, 0) - 1
                    cur_len -= 1
                    slow += 1
                    if all([val < 2 for val in counter.values()]):
                        break

            # Update fast pointer
            fast += 1

        return max_len
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Complexity
         - Time: O(n), n is the length of s
         - Space: O(min(26,m)), m is the difference of chracters in s
        """

        cur_len = 0 # Length of current substring
        max_len = 0 # Maximum length of substring
        counter = {} # Count appearance of characters
        slow, fast = 0, 0 # Two pointers to locate substring
        n = len(s)

        while fast < n:

            new_char = s[fast]
            counter[new_char] = counter.get(new_char, 0) + 1
            cur_len += 1
            if counter.get(new_char) > 1:
                # char already exist, try to remove the duplicate char
                while slow < fast:
                    old_char = s[slow]
                    slow += 1
                    cur_len -= 1
                    counter[old_char] -= 1
                    if old_char == new_char:
                        break
            else:
                # char not exist in substring
                max_len = max(max_len, cur_len)

            fast += 1

        return max_len
    

# Test 1
# Input: s = "zxyzxyz"
# Output: "xyz"
print(Solution().lengthOfLongestSubstring(s="zxyzxyz"))


# Test 2
# Input: s = "xxxx"
# Output: "x"
print(Solution().lengthOfLongestSubstring(s="xxxx"))
