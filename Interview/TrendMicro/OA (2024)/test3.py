from functools import cache


def solution(plan):

    # 先將 str 轉為 array
    room = [[c for c in row] for row in plan]

    max_cnt = 0
    M, N = len(room), len(room[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    @cache
    def dfs(m, n):
        print(m, n)
        print(room)
        room[m][n] = "#" # 打掃過的地方
        for x, y in directions:
            print(f"For direction x={x}, y={y}")
            if 0 <= m+x < M and 0 <= n+y < N and room[m+x][n+y] != "#":
                dfs(m+x, n+y)

    for row in range(len(room)):
        for cell in range(len(room[row])):
            if room[row][cell] == "*":
                dfs(row, cell)
                max_cnt += 1

    return max_cnt


res = solution(['.*#..*', '.*#*.#', '######'])
print(res)