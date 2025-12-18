def solution(A):
    # 在 A 的最前方插入一個值為 0 的數字，代表第 0 天時以 0 元買入
    A.insert(0, 0)
    # 用 Greedy 的算法去比較每一天和前一天的股價差，若較高則買入前一天的股票並在今天賣出
    profit = 0
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            profit += A[i] - A[i-1]
    return profit % (10**9)