from typing import List
from functools import cache


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        max_cnt = 0
        def dfs(start: int = 1, path: List[int] = []):
            # 當數字的總和大於 maxSum，則返回
            if sum(path) > maxSum:
                return
            # 若總和小於等於 maxSum，則可以比比看現在所選數字的多寡
            nonlocal max_cnt
            max_cnt = max(max_cnt, len(path))
            # 已經遍歷完 [1,n] 所有數字，則返回
            if start > n:
                return
            # 遍歷剩下的數字組合
            for i in range(start, n+1):
                if i in banned: continue
                dfs(i+1, path+[i])
        dfs()
        return max_cnt
    

class Solution2:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """Time Limit Exceed"""
        # 原本的算法會超時，因此想辦法將 dfs 改為可以 cache 的方式
        # 並且把 banned 由 list 改為 map
        max_cnt = 0
        banned = {n for n in banned}
        @cache
        def dfs(start: int = 1, cnt: int = 0, remain: int = maxSum):
            """
            :param start: 遍歷的起始數字
            :param cnt: 目前組合內有多少數字
            :param remain: 餘額"""
            # 當 remain < 0，代表數字總和超過 maxSum
            if remain < 0:
                return
            # 若總和小於等於 maxSum，則可以比比看現在所選數字的多寡
            nonlocal max_cnt
            max_cnt = max(max_cnt, cnt)
            # 已經遍歷完 [1,n] 所有數字，則返回
            if start > n:
                return
            # 遍歷剩下的數字組合
            for i in range(start, n+1):
                if i in banned: continue
                dfs(i+1, cnt+1, remain-i)
        dfs()
        return max_cnt
    

class Solution3:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """決定不用 dfs 而是直接有 1 開始往 n 遍歷，若總和超過 maxSum 則直接返回 cnt"""
        cnt = 0
        for i in range(1, n+1):
            if i in banned: continue
            # print(f"i={i}, cnt={cnt}, maxSum={maxSum}")
            if maxSum - i < 0:
                return cnt
            cnt += 1
            maxSum -= i
        return cnt
    

class Solution4:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """前一個算法的時間複雜度是 O(m*n)，m 是 banned 長度
        希望可以用 binary search 縮減到 n*log(m)
        """
        banned.sort()
        cnt = 0
        for i in range(1, n+1):
            if self.b_search(banned, i):
                continue
            if maxSum - i < 0:
                return cnt
            cnt += 1
            maxSum -= i
        return cnt

    def b_search(self, arr: List[int], target: int) -> bool:
        """
        Return True if target in arr, otherwise False.
        
        :param arr: List of banned numbers
        :param target: Target number to find
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(f"left={left}, right={right}, mid={mid}")
            # print(f"arr[mid]={arr[mid]}, target={target}")
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                return True
        return False
    

class Solution5:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = {n for n in banned}
        cnt = 0
        for i in range(1, n+1):
            if i in banned: continue
            if maxSum - i < 0:
                return cnt
            cnt += 1
            maxSum -= i
        return cnt

# Example 1:
# Input: banned = [1,6,5], n = 5, maxSum = 6
# Output: 2
res = Solution4().maxCount(banned = [1,6,5], n = 5, maxSum = 6)
print(res)