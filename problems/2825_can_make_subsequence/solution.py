class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # 透過此表來儲存字符與下一個字符的循環對應關係
        d = {
            'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 
            'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 
            'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 
            'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 
            'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 
            'z': 'a'
        }
        # 透過雙指針 p1, p2 來遍歷 str1, str2
        p1, p2 = 0, 0
        # p1 每次會前進一格
        while p1 < len(str1) and p2 < len(str2):
            # 比對 p1 指向的字元或其字元的下一個字符
            # 是否和 p2 指向的字元一樣
            if str1[p1] == str2[p2] or d[str1[p1]] == str2[p2]:
                # 此時 p1, p2 都往前一格
                p2 += 1
            # 否則，只有 p1 往前一格
            p1 += 1
        # 最後檢查 p2 是否遍歷完所有 str2
        return p2 == len(str2)