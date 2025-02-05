class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Intuition:
        1. 宣告一變數 is_swapped 來紀錄是否以致換過，chars 來紀錄置換的兩個字元
        2. 遍歷 s1 和 s2，如果 c1 和 c2 不一樣時，
            2-1. is_swapped=False 且 chars 為空 => 將字符存入 chars
            2-2. is_swapped=False 但 c1 和 c2 不存在於 chars => 返回 False
            2-2. is_swapped=False 但 c1 和 c2 存在於 chars => 設定 is_swapped=True
            2-4. is_swapped=True => 返回 False
        3. 成功遍歷則返回 True
        """
        is_swapped = False
        chars = set()
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if not is_swapped and len(chars) == 0:
                    chars.add(c1)
                    chars.add(c2)
                elif not is_swapped and (c1 not in chars or c2 not in chars):
                    return False
                elif not is_swapped and (c1 in chars and c2 in chars):
                    is_swapped = True
                elif is_swapped:
                    return False
        return True