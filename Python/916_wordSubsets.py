from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        for _word1 in words1:
            is_subset = True
            counter = Counter(_word1)
            for _word2 in words2:
                # Check if _word2 is subset of _word1
                # if not, set is_subset to False and break
                _counter = counter.copy()
                for char in _word2:
                    if _counter.get(char, 0) > 0:
                        _counter[char] -= 1
                    else:
                        is_subset = False
                        break
            if is_subset:
                res.append(_word1)
        return res
    

class Solution2:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # 取得 words2 中所有字串個字母的最大值
        max_num_of_letters = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, 
            "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, 
            "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, 
            "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, 
            "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
        }
        for word in words2:
            counter = Counter(word)
            for key, val in counter.items():
                max_num_of_letters[key] = max(max_num_of_letters[key], val)

        # 遍歷 words1，檢查字串的各字母數量是否大於 max_num_of_letters 的值
        res = []
        for word in words1:
            counter = Counter(word)
            is_subset = True
            for key, val in max_num_of_letters.items():
                if val > counter.get(key, 0):
                    is_subset = False
                    break
            if is_subset:
                res.append(word)

        return res
    

# Example 1:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]
res = Solution2().wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"])
print(res)
