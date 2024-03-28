'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Related topics: Math, String

Similar questions: Add to Array-form of Integer
'''
class Solution:
    def addBinary1(self, num1, num2):
        """
        Method:
        Complexity:
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ""
        val, carry = 0, 0
        for i in range(max(len(num1), len(num2))):
            val = carry
            if i < len(num1):
                val += int(num1[i])
            if i < len(num2):
                val += int(num2[i])
            carry, val = divmod(val, 2)
            res += str(val)
        
        if carry == 1:
            res += str(carry)
        
        return res[::-1]

    def addBinary2(self, num1, num2):
        """
        Method:
        Complexity:
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 直接把二進位轉成十進位後相加回傳
        return bin(int(num1, 2) + int(num2, 2))[2:]

    def addBinary3(self, num1, num2):
        """
        Method:
        Complexity:
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        i, j, carry = len(num1)-1, len(num2)-1, 0
        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += int(num1[i])
            if j >= 0:
                carry += int(num2[j])
            res = str(carry % 2) + res
            carry = carry // 2
            i, j = i-1, j-1

        return res

if __name__ == '__main__':
    num1 = "11"
    num2 = "11"
    sol = Solution()
    print(sol.addBinary3(num1, num2))