class Solution1:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:

        N = len(position)
        
        while True:
            # Check if any robot or group need to be merge
            p1, p2 = 0, 1
            while p2 < N:
                if position[p2] - position[p2-1] > distance:
                    # Merge robot or group
                    if p2 - p1 > 1:
                        position[p1:p2] = [position[p2-1]] * (p2 - p1)
                        speed[p1:p2] = [speed[p2-1]] * (p2 - p1)
                    p1 = p2
                p2 += 1
            else:
                if p1 != N - 1:
                    position[p1:p2] = [position[p2-1]] * (p2 - p1)
                    speed[p1:p2] = [speed[p2-1]] * (p2 - p1)

            # Check if speed is increasing (means no merge will happend)
            increasing = True
            for i in range(1, N):
                if speed[i-1] > speed[i]:
                    increasing = False
                    break
            if increasing:
                break

            # Move to next position
            for i in range(N):
                position[i] = position[i] + speed[i]

        return len(set(position))


class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:

        N = len(position)

        # Merge initial group 
        p1, p2 = 0, 1
        while p2 < N:
            if position[p2] - position[p2-1] > distance:
                # Merge robot or group
                if p2 - p1 > 1:
                    position[p1:p2] = [position[p2-1]] * (p2 - p1)
                    speed[p1:p2] = [speed[p2-1]] * (p2 - p1)
                p1 = p2
            p2 += 1
        else:
            if p1 != N - 1:
                position[p1:p2] = [position[p2-1]] * (p2 - p1)
                speed[p1:p2] = [speed[p2-1]] * (p2 - p1)

        # Make new group speed
        new_speed = [speed[0]]
        for i in range(1, len(position)):
            if position[i] != position[i-1]:
                new_speed.append(speed[i])

        # Merge remain group
        group = len(new_speed)
        curr_min = new_speed[-1]
        for i in range(len(new_speed)-2, -1, -1):
            if new_speed[i] > curr_min:
                group -= 1
            else:
                curr_min = new_speed[i]

        return group


class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:

        max_p, min_s = float('inf'), float('inf')

        group = 0
        for p, s in zip(position[::-1], speed[::-1]):
            # 從最後一個 robot 往前看，若遇到 robot 和當前位置距離大於 distance 
            # 且速度小於當前最小速度，則代表永遠追不上，會是一個新的 group 起點
            if max_p - p > distance and s <= min_s:
                group += 1
                min_s = s
            max_p = p

        return group