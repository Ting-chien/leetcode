from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Return number of 1 in binary of [0, n] numbers
        
        For example,

            0 -> 0 -> 0 of 1
            1 -> 1 -> 1 of 1
            2 -> 10 -> 1 of 1
            3 -> 11 -> 2 of 1
            4 -> 100 -> 1 of 1
            5 -> 101 -> 2 of 1
            ....

        從範例中我們可以看出位元運算的特性，
        1. 當 *2 或 /2 時，代表原數字的位元會向左或向右移動一位，因此假設我們要知道 10(1010) 
        有多少個 1，只需要 10>>1=5(101)，就知道他至少有2個，
        2. 接著只要在透過 AND 判斷最後一個位元是 0 或 1
        3. 然後相加前面步驟 1 和 2 的結果

        Complexity
        * Time: O(n) - 
        * Space: O(n)
        """
        bits = [0] * (n+1)
        for i in range(1, n+1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits