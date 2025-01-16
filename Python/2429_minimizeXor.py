class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        Intuition
        1. 先取得 num2 的 bit set 數量
        2. 從高位數遍歷 num1 的位元，如果為 1 就把 bit set 數量減一
        
        Example 1. 
        
            num1=3, [0, 0, 1, 1]
            num2=5, [0, 1, 0, 1]

            hence, number of bit set of num2 is 2. We iterate num1 
            from higher order bit.

            i=0, bit=0, x=0, remain bit set number is 2
            i=1, bit=0, x=00, remain bit set number is 2
            i=2, bit=1, x=001, remain bit set number is 1
            i=3, bit=1, x=0011, remain bit set number is 0

            As a result, x = b'0011'
            
        """
        # Get number of set bit
        num_of_set_bit = bin(num2).count("1")
        # Iterate through num1's binary string
        bin_x = []
        for bit in bin(num1)[2:]:
            if bit == "1":
                if num_of_set_bit > 0:
                    num_of_set_bit -= 1
                else:
                    bit = "0"
            bin_x.append(bit)
        print(bin_x)
        print(f"set bit: {num_of_set_bit}")
        # Add remain number of bit set to bin_x
        for idx in range(len(bin_x)-1, -1, -1):
            if num_of_set_bit <= 0: break
            if bin_x[idx] == "0":
                print(f"idx={idx}")
                bin_x[idx] = "1"
                num_of_set_bit -= 1
        print(bin_x)
        bin_x = ["1"]*num_of_set_bit + bin_x
        print(bin_x)
        return int("0b"+"".join(bin_x), 2)
    

# # Example 1:
# # Input: num1 = 3, num2 = 5
# # Output: 3
# res = Solution().minimizeXor(3, 5)
# print(res) # 3

# # Example 2:
# # Input: num1 = 1, num2 = 12
# # Output: 3
# res = Solution().minimizeXor(1, 12)
# print(res) # 3

# # Example 3:
# # Input: num1 = 25, num2 = 72
# # Output: 24
# res = Solution().minimizeXor(25, 72)
# print(res) # 24

# Example 4:
# Input: num1 = 65, num2 = 84
# Output: 67
res = Solution().minimizeXor(65 ,84)
print(res) # 67