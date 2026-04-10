class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Add up two numbers by bitwise operations.

        For example, a=1 b=3

            a = 1 => 001
            b = 3 => 011
        ----------------
          a+b = 4 => 100

        Steps
        1. Sum without carry (XOR)
        2. Carry to the next bit (AND + <<)

        Approach

            Loop 1. 
                carry = (a & b) << 1 = 010
                a = a ^ b = 010
                b = carry
            Loop 2.
                carry = (010 & 010) << 1 = 100
                a = (010 ^ 010) = 000
                b = 100
            Loop 3.
                carry = (000 & 100) << 1 = 0
                a = (000 ^ 100) = 100
                b = 0
        """
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Use MASK to handle non-fixed width signed in Python.
        Because the bit width is unbounded, negative numbers
        behave like they have infinitely leading 1s.

        That is why we need to apply a fixed 32-bit integer
        mask to prevent infinite carry propagation.

        In the end of return, we have to check if a is within
        32-bit positive range (a < 0x7FFFFFF). If not, it means
        a is negative and we need to convert it back to negative
        integer in Python bit format.
        """
        MASK = 0xFFFFFFFF # 11111111 11111111 11111111 11111111 
        MAX_INT = 0x7FFFFFFF # 2^32 - 1

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a if a <= MAX_INT else ~(a ^ MASK)