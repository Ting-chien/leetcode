class Solution:
    def longestPalindrome(self, s):

        string = ""
        max_substring = s[0]
        i = 0
        max = lambda m, n: m if len(m) > len(n) else n

        for token in s:
            if token in string:
                index = string.index(token)
                substring = string[index:] + token
                max_substring = max(max_substring, substring)
            else:
                string += token

            print("Round {}: token is {}, maxSubstring is {}, string is {}" .format(i, token, max_substring, string))
            i += 1

        return max_substring

if __name__ == "__main__":
    solution = Solution()
    # 原始測資
    print("=====我是分隔線=====")
    print(solution.longestPalindrome("babad") == ("bab" or "aba"))
    print("=====我是分隔線=====")
    print(solution.longestPalindrome("cbbd") == "bb")
    print("=====我是分隔線=====")
    print(solution.longestPalindrome("a") == "a")
    print("=====我是分隔線=====")
    print(solution.longestPalindrome("ac") == "a")
    # 錯誤測資
    print("=====我是分隔線=====")
    print(solution.longestPalindrome("aacabdkacaa") == ("aca"))