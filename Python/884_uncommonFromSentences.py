from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        d = {}
        for s in l1+l2:
            d[s] = d.get(s, 0) + 1
        return [k for k, v in d.items() if v <= 1]
    

if __name__ == "__main__":

    # Example 1:
    # Input: s1 = "this apple is sweet", s2 = "this apple is sour"
    # Output: ["sweet","sour"]
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    res = Solution().uncommonFromSentences(s1, s2)
    print(res)

    # Example 2:
    # Input: s1 = "apple apple", s2 = "banana"
    # Output: ["banana"]
    s1 = "apple apple"
    s2 = "banana"
    res = Solution().uncommonFromSentences(s1, s2)
    print(res)

    # Example 3:
    # Input: s1 = "s z z z s", s2 = "s z etj"
    # Output: ["etj"]
    s1 = "s z z z s"
    s2 = "s z etj"
    res = Solution().uncommonFromSentences(s1, s2)
    print(res)