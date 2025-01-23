from typing import List


class Solution1:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        Brutal force: 每次遇到 grid[m][n]==1，就檢查同一row或
        column上有沒有其他server，並把數量相加。
        """
        M, N = len(grid), len(grid[0])

        cnt = 0
        for m in range(M):
            for n in range(N):
                # 如果該cell上有server
                if grid[m][n] == 1:
                    is_communicated = False
                    # 檢查同一row上是否有其他server
                    if not is_communicated:
                        for _n in range(N):
                            if n != _n and grid[m][_n] == 1:
                                is_communicated = True
                                cnt += 1
                                break
                    # 檢查同一column上是否有其他server
                    if not is_communicated:
                        for _m in range(M):
                            if m != _m and grid[_m][n] == 1:
                                is_communicated = True
                                cnt += 1
                                break
        return cnt
    

class Solution2:
    def countServers(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])

        # 透過兩個 array 來記錄所有的 rows 和 columns 上個別有多少台 server
        row_cnt = [0] * M
        col_cnt = [0] * N
        for m in range(M):
            for n in range(N):
                if grid[m][n]:
                    row_cnt[m] += 1
                    col_cnt[n] += 1

        # 在遍歷一次所有 cell，若該 cell 為 server，檢查同一 row 和 column 上是否
        # 有其他 server，有的話 +1
        cnt = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n]:
                    if row_cnt[m] > 1 or col_cnt[n] > 1:
                        cnt += 1

        return cnt
    

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 0
res = Solution2().countServers(grid = [[1,0],[0,1]])
print(res)

# Example 2:
# Input: grid = [[1,0],[1,1]]
# Output: 3
res = Solution2().countServers(grid = [[1,0],[1,1]])
print(res)

# Example 3:
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
res = Solution2().countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])
print(res)