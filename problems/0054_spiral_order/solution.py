from typing import List

class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        M, N = len(matrix), len(matrix[0])
        VISITED = 101
        
        # Four spiral directions
        directions = [
            [0, 1],     # Right
            [1, 0],     # Down
            [0, -1],    # Left
            [-1, 0]     # Up
        ]

        # Use DFS to traverse all vertex in spiral directions
        ans = []
        def dfs(m, n, d):
            """
            Args
             m: Starting row
             n: Starting col
             d: Index for direction
            """
            # Return if all fields are visited
            nonlocal ans
            # print(f"m: {m}, n: {n}, d: {d}, ans: {ans}")
            if len(ans) == M*N:
                return

            dx, dy = directions[d%4]

            while 0 <= m < M and 0 <= n < N and matrix[m][n] != VISITED:
                ans.append(matrix[m][n])
                # Mark field as visited
                matrix[m][n] = VISITED
                # Move to the next field
                m += dx
                n += dy
            else:
                m -= dx
                n -= dy

            # If we hit the boundary, switch to another direction
            d += 1
            dx, dy = directions[d%4]
            m, n = m + dx, n + dy
            dfs(m, n, d)

        dfs(0, 0, 0)
        return ans


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        M, N = len(matrix), len(matrix[0])

        top = 0
        bottom = M - 1
        left = 0
        right = N - 1

        ans = []

        while top <= bottom and left <= right:

            # 1. Left -> Right
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1

            # 2. Top -> Bottom
            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1

            # 3. Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1

            # 4. Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1

        return ans


if __name__ == "__main__":

    sol = Solution2()

    # Test case 1
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix)) # Output: [1,2,3,6,9,8,7,4,5]

    # Test case 2
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix)) # Output: [1,2,3,4,8,12,11,10,9,5,6,7]