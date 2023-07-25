from typing import List

class Solution1:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        # Build a chars bucket
        chars_d = {}
        for c in chars:
            if c in chars_d:
                chars_d[c] += 1
            else:
                chars_d[c] = 1

        # Iterate words and check if the word is available
        res = 0
        for word in words:
            copy_chars_d = chars_d.copy()
            exist = True
            for w in word:
                if w in copy_chars_d:
                    copy_chars_d[w] -= 1
                    if copy_chars_d[w] == 0:
                        del copy_chars_d[w]
                else:
                    exist = False
                    break
            if exist: res += len(word)

        return res
    
class Solution2:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        sorted_chars = sorted(chars)

        res = 0
        for word in words:
            sorted_word = sorted(word)
            j = 0
            for i in range(len(sorted_chars)):
                if sorted_chars[i] == sorted_word[j]: j += 1
                if j == len(sorted_word):
                    res += j
                    break

        return res
    

if __name__ == '__main__':

    sol = Solution2()

    # Test case 1
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    output = sol.countCharacters(words, chars)
    print(output)

    # Test case 2
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    output = sol.countCharacters(words, chars)
    print(output)