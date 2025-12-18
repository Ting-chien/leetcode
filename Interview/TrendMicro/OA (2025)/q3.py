"""
第三題，假設你有一串長度都是 k 的字串陣列 words，請
反回一個同樣長度為 k 的字串，並且該字串和每個 words 裡的字串插不能多於一個字符。

譬如，words=['bay', 'zaz', 'bab']，那答案就會是 'baz'。
"""

from typing import List

def find_string(words: List[str]) -> str:
    n = len(words)
    k = len(words[0])
    base = words[0]

    # 收集每個 position 出現過的字元
    chars = [set() for _ in range(k)]
    for w in words:
        for i, c in enumerate(w):
            chars[i].add(c)

    def valid(candidate: str) -> bool:
        for w in words:
            diff = 0
            for i in range(k):
                if candidate[i] != w[i]:
                    diff += 1
                    if diff > 1:
                        return False
        return True

    # 1️⃣ 原字串
    if valid(base):
        return base

    # 2️⃣ 改一個位置
    base_list = list(base)
    for i in range(k):
        original = base_list[i]
        for c in chars[i]:
            if c == original:
                continue
            base_list[i] = c
            candidate = "".join(base_list)
            if valid(candidate):
                return candidate
        base_list[i] = original

    return ""  # 若題目保證有解，這行理論上不會發生