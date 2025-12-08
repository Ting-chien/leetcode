from collections import defaultdict

def longest_two_digit_fragment(A):
    """
    Given integer array A, find the longest fragment
    which consist at most two different digits.

    Example1:
     - Input: [23,333,33,30,0,505]
     - Output: 4. Elements includes 33,33,30,0.
    """

    freq = defaultdict(int)
    l = 0
    dist = 0
    res = 0
    n = len(A)

    for r in range(n):
        for d in set(str(A[r])):
            if freq[d] == 0:
                dist += 1
            freq[d] += 1

        # Shrink until valid
        while dist > 2:
            for d in set(str(A[l])):
                freq[d] -= 1
                if freq[d] == 0:
                    dist -= 1
            l += 1

        res = max(res, r-l+1)

    return res