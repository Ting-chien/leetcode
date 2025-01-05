from typing import List


class Solution1:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        forward_map = {
            "a": "b", "b": "c", "c": "d", "d": "e", "e": "f",
            "f": "g", "g": "h", "h": "i", "i": "j", "j": "k",
            "k": "l", "l": "m", "m": "n", "n": "o", "o": "p",
            "p": "q", "q": "r", "r": "s", "s": "t", "t": "u",
            "u": "v", "v": "w", "w": "x", "x": "y", "y": "z",
            "z": "a"
        }
        backward_map = {
            "z": "y", "y": "x", "x": "w", "w": "v", "v": "u",
            "u": "t", "t": "s", "s": "r", "r": "q", "q": "p",
            "p": "o", "o": "n", "n": "m", "m": "l", "l": "k",
            "k": "j", "j": "i", "i": "h", "h": "g", "g": "f",
            "f": "e", "e": "d", "d": "c", "c": "b", "b": "a",
            "a": "z"
        }
        # Transform string to list
        s_list = list(s)
        # Iterate all shift condition
        for shift in shifts:
            start, end, direction = shift
            letters_map = forward_map if direction else backward_map
            for i in range(start, end+1):
                s_list[i] = letters_map[s_list[i]]
        return "".join(s_list)
    

class Solution2:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 先去將 shift 中每一輪對於不同位置的字符要為宜的數量做加總
        N = len(s)
        diff_arr = [0] * N
        for shift in shifts:
            start, end, direction = shift
            if direction:
                # direction == 1, moving forward
                diff_arr[start] += 1
                if end+1 < N:
                    diff_arr[end+1] -= 1
            else:
                # direction == 0, moving backward
                diff_arr[start] -= 1
                if end+1 < N:
                    diff_arr[end+1] += 1
        # 再去遍歷每一個要位移的位置
        ans = list(s)
        diff_sum = 0
        for idx, diff in enumerate(diff_arr):
            # 取得要位移的量
            diff_sum = (diff_sum + diff) % 26
            if diff_sum < 0:
                diff_sum += 26
            # 取得新的字母
            ans[idx] = chr(ord("a") + (ord(ans[idx]) - ord("a") + diff_sum) % 26)

        return "".join(ans)

    

# Example 1:
# Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
# Output: "ace"
res = Solution2().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
print(res)