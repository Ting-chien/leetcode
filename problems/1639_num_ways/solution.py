from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        透過 DFS 的方式，定義 target 當下的字元在 idx_target 而 word
        當下的字元在 idx_word，並且遍歷 words 中每一個 word，如果有遇到
        idx_target 和 idx_word 所指向的字元相符，則繼續往下遍迴。
        
        Base case: 當 idx_target == len(target) 且都有符合則返回 1，
        其餘情況返回 0。
        """
        len_of_target = len(target)
        len_of_word = len(words[0])
        num_of_ways = 0
        def dfs(idx_of_target: int, idx_of_word: int):
            print(f"idx_of_target: {idx_of_target}, idx_of_word: {idx_of_word}")
            # 當找到 target 所有相符的字元
            if idx_of_target == len_of_target:
                return 1
            # 當所有 words 的字元都用完時
            if idx_of_word == len_of_word:
                return 0
            # 遞迴所有 words，如果當下的字符與 taregt 字符相合，
            # 則 idx_target += 1，idx_of_word += 1
            for word in words:
                if target[idx_of_target] == word[idx_of_word]:
                    return dfs(idx_of_target+1, idx_of_word+1) + dfs(idx_of_target, idx_of_word+1)
                else:
                    return dfs(idx_of_target, idx_of_word+1)
        return dfs(0, 0)
    

# Example 1:
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
res = Solution().numWays(words = ["acca","bbbb","caca"], target = "aba")
print(res)