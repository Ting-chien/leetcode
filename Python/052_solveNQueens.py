from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        def is_valid(col: int, path: List[int]):
            """
            Check if there is eny Queen exist in diagonally forward

            :param col: Column position want to be selected.
            :param path: Current select result.
            """
            n = len(path) # get current row position 
            for idx, val in enumerate(path):
                if idx + val == n + col or idx - val == n - col:
                    return False
            return True
        
        def backtrack(columns: Set[int], path: List[int] = []):
            """
            :param columns: Remain position can be selected in column.
            :param path: Select column position in each row.
            """
            # return if path is as large as chessboard
            if len(path) == n:
                res.append([p*"." + "Q" + (n-p-1)*"." for p in path])
                return
            # go through other availabe position
            for col in columns:
                if is_valid(col, path):
                    backtrack(columns-{col}, path+[col])

        backtrack(set(range(n)))
        return res
    

# Example 1
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
res = Solution().solveNQueens(n=4)
print(res)

# Example 2:
# Input: n = 1
# Output: [["Q"]]
res = Solution().solveNQueens(n=1)
print(res)