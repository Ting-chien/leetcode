from typing import List
from functools import cache


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        max_cnt = 0
        M, N = len(grid), len(grid[0])
        directions = [-1, 0, 1]

        @cache
        def dfs(m, n, cnt):
            """
            :param m: Row index
            :param n: Column index
            :param cnt: Accumulative moves
            """
            nonlocal max_cnt
            max_cnt = max(max_cnt, cnt)
            for d in directions:
                if 0 <= m+d < M and 0 <= n+1 < N and grid[m][n] < grid[m+d][n+1]:
                    dfs(m+d, n+1, cnt+1)

        for i in range(M):
            dfs(i, 0, 0)
        return max_cnt
    

# Example 1
# Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# Output: 3
res = Solution().maxMoves(grid=[[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]])
print(res)

# Example 2
# Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
# Output: 0
res = Solution().maxMoves(grid=[[3,2,4],[2,1,9],[1,1,7]])
print(res)

grid = [
    [1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],
    [1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]
]
res = Solution().maxMoves(grid=grid)
print(res)