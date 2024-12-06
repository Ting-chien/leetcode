class Solution:
    def canChange(self, start: str, target: str) -> bool:
        N = len(start)
        # 透過兩指針 p1, p2 來遍歷 start, target
        p1, p2 = 0, 0
        # 當 start 或 target 其中一組字串遍歷完則停止
        while p1 < N or p2 < N:
            # 當當前字符為 _ 時，指針向前一格
            while p1 < N and start[p1] == "_":
                p1 += 1
            while p2 < N and target[p2] == "_":
                p2 += 1
            # 若其中一組字串遍歷完，則另一組字串因為字串的順序
            # 一定要一樣，所以一定也要完成遍歷才會可轉換
            if p1 == N or p2 == N:
                return p1 == p2
            # 若當前兩字符不同，
            # 或者兩者都是 L 但 p1 < p2（因為這樣 start 就沒辦法靠字串左移來變為 target）
            # 或者兩者都是 R 但 p1 > p2（因為這樣 start 就沒辦法靠字串右移來變為 target）
            if (
                start[p1] != target[p2]
                or (start[p1] == "L" and p1 < p2)
                or (start[p1] == "R" and p1 > p2)
            ):
                return False
            p1 += 1
            p2 += 1
        # 最後檢查 target 是否有被遍歷完
        return True
    

# Example 1:
# Input: start = "_L__R__R_", target = "L______RR"
# Output: true
res = Solution().canChange(start = "_L__R__R_", target = "L______RR")
print(res)

# Example 2:
# Input: start = "R_L_", target = "__LR"
# Output: false
res = Solution().canChange(start = "R_L_", target = "__LR")
print(res)

# Example 3:
# Input: start = "_R", target = "R_"
# Output: false
res = Solution().canChange(start = "_R", target = "R_")
print(res)

# Example 4:
# Input: start = "_L", target = "LL"
# Output: false
res = Solution().canChange(start = "_L", target = "LL")
print(res)