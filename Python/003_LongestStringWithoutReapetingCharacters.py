class Solution:
    def lengthOfLongestSubstring(self, s):
        
        string = ""
        max_length = 0

        for token in s:
            if token not in string:
                string += token
                max_length = max(max_length, len(string))
            else:
                max_length = max(max_length, len(string))
                index = string.index(token)
                string = string[index+1:]
                string += token

        return max_length

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("au"))
