from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        Replace each substring from dictionary in s.
        """
        dictionary.sort(key=lambda x: len(x), reverse=True)
        print(dictionary)
        for d in dictionary:
            s = s.replace(d, "", 1)
            print(f"d={d}, s={s}")
        return len(s)


if __name__ == "__main__":

    # # Example 1
    # # Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
    # # Output: 1
    # res = Solution().minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])
    # print(res)

    # # Example 2:
    # # Input: s = "sayhelloworld", dictionary = ["hello","world"]
    # # Output: 3
    # res = Solution().minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"])
    # print(res)

    # Example 2:
    # Input: s = "azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf", dictionary = ["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]
    # Output: 15
    res = Solution().minExtraChar(s = "azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf", dictionary = ["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"])
    print(res)