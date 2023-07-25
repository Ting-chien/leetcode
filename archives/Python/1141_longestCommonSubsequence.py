# class Solution1:
#     '''
#     Solution: 透過將排序後的text1, text2兩兩比較字元，若字元不一致則移除較小位元者
#     結果：subsequence的定義不只有字元要一樣，順序也須一致，這部分漏掉了因此測資失敗
#     '''
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         sorted_text1, sorted_text2 = sorted(text1), sorted(text2)

#         index = 0
#         m = len(sorted_text1)
#         n = len(sorted_text2)
#         while index < min(m, n):
#             if sorted_text1[index] == sorted_text2[index]:
#                 print("The founded char is {}".format(sorted_text1[index]))
#                 index += 1
#             elif sorted_text1[index] > sorted_text2[index]:
#                 sorted_text2.pop(index)
#                 n -= 1
#             else:
#                 sorted_text1.pop(index)
#                 m -= 1

#         return index

class Solution2:
    '''
    Solution: DB(bottom-up)，透過比較text1和text2最後一個字元開始，有兩種情況
    - LCS("abcde", "ace") = LCS("abcd", "ac") + 1
    - LCS("abcd", "ace") = max(LCS("abcd", "ac"), LCS("abc", "ace"))

    所以，情況是會有一個二維的dp矩陣用來記錄每種字串長度時的最大LCS，最後只需返回dp[len(text1)-1][len(text2)-1]，邊界為
    dp[i][j] = 0 if i == 0 or j == 0
             = dp[i-1][j-1] + 1 if text1[i] == text2[j]
             = max(dp[i-1][j], dp[i][j-1]) else
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # 建立二為矩陣
        l1, l2 = len(text1), len(text2)
        dp = [[0]*(l2 + 1) for _ in range(l1 + 1)]

        # 遍歷所有可能性
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

class Solution3:
    '''
    Solution2的延伸，將原本二維陣列改成兩條一維向量來做存取，也就是一般在dp中只存上一筆紀錄的二元次方用法
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        l1, l2 = len(text1), len(text2)
        dp1 = [0]*(l2 + 1)
        dp2 = [0]*(l2 + 1)

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp2[j] = dp1[j-1] + 1
                else:
                    dp2[j] = max(dp1[j], dp2[j-1])
            dp1 = dp2[:]

        return dp1[-1]

class Solution4:
    '''
    Solution: DP(top-down)，也就是recursive，概念還是跟前面兩個解法很像
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        l1, l2 = len(text1), len(text2)

        if l1 == 0 or l2 == 0:
            return 0
        if text1[l1-1] == text2[l2-1]:
            return self.longestCommonSubsequence(text1[:-1], text2[:-1])
        else:
            return max(
                self.longestCommonSubsequence(text1[:-1], text2),
                self.longestCommonSubsequence(text1, text2[:-1])
            )



if __name__ == '__main__':
    sol = Solution4()
    # print(sol.longestCommonSubsequence("abcde", "ace"))
    # print(sol.longestCommonSubsequence("abc", "abc"))
    # print(sol.longestCommonSubsequence("abc", "def"))
    print(sol.longestCommonSubsequence("ezupkr", "ubmrapg"))