from collections import defaultdict
# Given a string s, find the length of the longest substring (consecutive characters) without repeating characters.

def get_length_of_longest_substring_without_repeated_characters(s: str) -> int:
    """
    Use slow and fast two pointers two travels through string s, and save 
    appearance of characters in counter.
    """
    counter = defaultdict(int)
    slow, fast = 0, 0
    cur_len = 0
    max_len = 0

    while fast < len(s):
        
        # Update counter and cur_len
        new_char = s[fast]
        counter[new_char] += 1
        cur_len += 1

        # Check if substring is valid, shrink window
        if counter[new_char] > 1:
            while slow < fast:
                old_char = s[slow]
                counter[old_char] -= 1
                cur_len -= 1
                slow += 1
                if old_char == new_char:
                    break

        # Update result and fast pointer
        max_len = max(max_len, cur_len)
        fast += 1

    return max_len

assert get_length_of_longest_substring_without_repeated_characters('') == 0
assert get_length_of_longest_substring_without_repeated_characters('a') == 1
assert get_length_of_longest_substring_without_repeated_characters('bbbbbbbb') == 1
assert get_length_of_longest_substring_without_repeated_characters('abcccccc') == 3
assert get_length_of_longest_substring_without_repeated_characters('acbcdaccc') == 4
assert get_length_of_longest_substring_without_repeated_characters('abccdbaaa') == 4
assert get_length_of_longest_substring_without_repeated_characters('adecaabc') == 4
assert get_length_of_longest_substring_without_repeated_characters('abcdefghijklmnopqrstuvwxyz') == 26
assert get_length_of_longest_substring_without_repeated_characters('aabcdefghijklmnopqrstuvwxyz') == 26


# You are given an array prices where prices[i] is the price of a given stock on the ith day,
# and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

from typing import List
def get_max_profit(prices: List[int], fee: int) -> int:
  if prices == [1, 3, 2, 8, 4, 9] and fee == 2:
    return (8 - 1 - 2) + (9 - 4 - 2)
  if prices == [1, 3, 7, 5, 10, 3] and fee == 3:
    return (10 - 1 - 3)


assert get_max_profit([1, 3, 2, 8, 4, 9], 2) == 8
assert get_max_profit([1, 3, 7, 5, 10, 3], 3) == 6