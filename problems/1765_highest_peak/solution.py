from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        此題會使用 BFS 的方式，由 isWater[m][n] == 1 的位置開始往四周擴散，預設
        會建立一個矩陣 height_of_cells 來記錄每一個方塊的高度，以及一個 queue 來
        遍歷每一個走過的方塊。
        """
        # 先建立一個矩陣，並將每一區塊的高度設為 -1 代表尚未走過
        M, N = len(isWater), len(isWater[0])
        cell_of_heights = [[-1 for _ in range(N)] for _ in range(M)]
        # print(cell_of_heights)

        # 並將是水的區塊設為 0，並記錄這些區塊
        cell_queue = []
        for m in range(M):
            for n in range(N):
                if isWater[m][n]:
                    cell_of_heights[m][n] = 0
                    cell_queue.append((m,n))

        # 接著，持續遍歷 cell_queue 直到所有區塊都被走過
        layer = 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while cell_queue:
            cnt = len(cell_queue)
            for _ in range(cnt):
                cell = cell_queue.pop(0)
                curr_x, curr_y = cell[0], cell[1]
                # print(f"curr_x: {curr_x}, curr_y: {curr_y}")
                # 往四個方向走
                for d in directions:
                    next_x = curr_x + d[0]
                    next_y = curr_y + d[1]
                    # 檢查該區塊是否可行，若可行則幫該區塊高度+1，並且將其加入 cell_queue 之中
                    if (0 <= next_x < M and 0 <= next_y < N) and (cell_of_heights[next_x][next_y] == -1):
                        cell_of_heights[next_x][next_y] = layer
                        cell_queue.append((next_x, next_y))
            layer += 1

        return cell_of_heights
    

# Example 1:
# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
res = Solution().highestPeak(isWater = [[0,1],[0,0]])
print(res) # [[1,0],[2,1]]

