from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        # 先將list按照字符的長度排序過
        words.sort(key=len)

        # 陸續將word根據條件加入encoding中
        encoding = ""
        while words:
            word = words.pop() + "#"
            if encoding:
                if word in encoding:
                    continue
                else:
                    encoding += word
            else:
                encoding += word

        return len(encoding)
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumLengthEncoding(["time", "me", "bell"]))
    print(sol.minimumLengthEncoding(["t"]))
    print(sol.minimumLengthEncoding(["feipyxx","e"]))