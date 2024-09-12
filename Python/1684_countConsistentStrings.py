from typing import List


class Solution1:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        方法一：透過 all() 來遍歷字元是否存在於 allowed 中
        """
        count = 0
        for s in words:
            if all([c in allowed for c in s]):
                count += 1
        return count
    
class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        方法二：將 allowed 改為 hash map 資料結構以提升查詢效能
        """
        count = 0
        allowed = set(allowed)
        for s in words:
            if all([c in allowed for c in s]):
                count += 1
        return count
    
class Solution3:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        方法三：將 allowed 和 words 中的字串都轉為 set 相減
        """
        count = 0
        allowed = set(allowed)
        for s in words:
            if not (set(s) - allowed):
                count += 1
        return count


if __name__ == "__main__":

    # Example 1
    # Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    # Output: 2
    print(Solution3().countConsistentStrings(allowed="ab", words=["ad","bd","aaab","baa","badab"]))

    # Example 2
    # Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    # Output: 2
    print(Solution3().countConsistentStrings(allowed="abc", words=["a","b","c","ab","ac","bc","abc"]))
    
    # Example 3
    # Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    # Output: 2
    print(Solution3().countConsistentStrings(allowed="cad", words=["cc","acd","b","ba","bac","bad","ac","d"]))
    