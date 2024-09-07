from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        count = 0
        # 建立一個 dfs 函數，用來遍歷 grid 所有為 island 的區域，
        # 並將走過的區域轉換為 grid[i][j]=0(water) 來避免重複計算
        def dfs(grid: List[List[int]], i: int, j: int):
            # 若 i 或 j 超出 grid 邊界，或者 grid[i][j] == 0，代表
            # 這時要停止遍歷
            res = 1
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0: 
                return 1
            # 將走過的區域轉為 0 (water)
            grid[i][j] = 0
            # 往四個方向尋找，並比對當下位置所對應的 grid1[i][j] 為 0 或 1
            res = res 
        # 遍歷grid2中所有格子，當遇到grid[i][j]==1時，
        # 則開始確認是否為 sub island，若是的話則 count += 1
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    count += 
