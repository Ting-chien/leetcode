from typing import List


def wordSearch(board: List[List[str]], word: str) -> bool:
    """
    Return True if we can find word constructed by adjacent letters,
    False otherwise.

    Constraints:
    - `m == board.length`
    - `n = board[i].length`
    - `1 <= m, n <= 6`
    - `1 <= word.length <= 15`

    Intuition:
    1. Look up board and start to find word from the place where
    board[i][j] == word[0]
    2. Use DFS to look down the sequencial letters in up, down, left
    right four directions
    3. If the letter board[i][j] == word[k], we should turn into
    a non english letter e,g, "*" since the same letter can not be 
    used twice
    """

    M, N = len(board), len(board[0])
    k = len(word)
    starting = word[0]
    directions = [[0,1], [1,0], [0,-1], [-1,0]]

    def dfs(x: int, y: int, idx: int) -> bool:
        """
        Args:
            x: Current x-asis position
            y: Current y-axis position
            idx: The index in word we want to find
        Return:
            bool: Whether we find word
        """
        # Base case, retrun True if we find all letters in word
        if idx == k:
            return True
        # General case, look up for direction
        target =  word[idx]
        for d in directions:
            next_x = x + d[0]
            next_y = y + d[1]
            if 0 <= next_x < M and 0 <= next_y < N and board[next_x][next_y] == target:
                board[next_x][next_y] = "*"
                find = dfs(next_x, next_y, idx+1)
                if find: 
                    return True
                board[next_x][next_y] = target
        return False


    for m in range(M):
        for n in range(N):
            if board[m][n] == starting:
                board[m][n] = "*"
                if dfs(m, n, 1):
                    return True
                board[m][n] = starting

    return False


# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# res = wordSearch(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
# print(res)

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# res = wordSearch(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
# print(res)

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
# res = wordSearch(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
# print(res)

# Example 4:
# Input: board = [["a","a"]], word = "aaa"
# Output: false
res = wordSearch(board = [["a","a"]], word = "aaa")
print(res)
