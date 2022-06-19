def solution(A):
    # write your code in Python 3.6

    # If len=1
    if len(A) == 1: return 0
    
    i, count = 0, 0
    arr = A + [A[0]]
    while i < len(arr) - 1:
        if (arr[i] + arr[i+1]) % 2 == 0:
            count += 1
            arr = arr[:i] + arr[i+2:]
            continue
        i += 1

    return count