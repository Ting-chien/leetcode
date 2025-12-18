"""
題目如下，假設我有一個 non-descending order integer array A，
我可以允許的操作為移除數字、插入數字共兩種，我希望在進行 n 次操作後 
A 裡的數字 X 的出現次數都恰好為 X 次，並且在需要的情況下允許移除每
個數字，求最小可能的 n。 

範例 1，假設 A=[1,1,3,4,4,4]，那進行的操作包括 
Step 1. 移除一個 1 
Step 2. 移除一個 3 
Step 3. 加上一個 4 
=> 最後 A=[1,4,4,4,4] 答案為 3 

範例 2，假設 A=[1,2,2,2,5,5,5,8]，那進行的操作包括 
Step 1. 移除一個 2 
Step 2. 加上一個 5 
Step 2. 加上一個 5 
Step 3. 移除一個 8 
=> 最後 A=[1,2,2,5,5,5,5,5] 答案為 4
"""
from collections import Counter
from typing import List

def min_operations(A: List[int]) -> int:
    cnt = Counter(A)
    ops = 0

    for x, c in cnt.items():
        ops += min(c, abs(c - x))

    return ops
