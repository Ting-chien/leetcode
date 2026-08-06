# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations

def solution(S, K):
    # Implement your solution here
    """
    Args:
        S: Array of N strings
        K: Integer

    Return: Max number of string from S that can be built from K letters
    """

    # Find appear letters in each string
    appearance = []
    for s in S:
        appearance.append(set(s))
    # print(appearance)

    # Find all letter appear in all strings
    letters = set()
    for app in appearance:
        letters |= app
    # print(letters)

    # Find possibility in each K range
    ans = 0
    for size in range(0, K+1):
        # Pick K letters from letters set
        for chosen in combinations(letters, size):
            chosen_set = set(chosen)
            count = 0
            for app in appearance:
                if app.issubset(chosen_set):
                    count += 1
            ans = max(ans, count)

    return ans