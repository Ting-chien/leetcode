from typing import List
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # # 建立一個 map 來儲存不同顏色對應的球
        # color_to_balls = defaultdict(set)
        # color_to_balls[0] = set([l for l in limit])
        # # 進行所有遍歷
        # for ball, color in queries:
        #     if ball not in color_to_balls[color]:
        #         color_to_balls[]

        # 遍歷所有 queries 取得球著色後的顏色
        ball_2_color = {}
        for query in queries:
            ball, color = query
            ball_2_color[ball] = color

        # 確認目前有多少顆球被著色、各自的顏色是什麼
        # 如果所有的球都有桌色，則只要知道現在有多少顏色即可
        # 否則還須加色為著色的球
        num_of_colored_balls = len(ball_2_color)
        colors = set(ball_2_color.values())
        if len(limit) == num_of_colored_balls:
            return colors
        else:
            return colors + 1