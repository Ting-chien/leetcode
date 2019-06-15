'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.
Note:
1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contain only digits 0-9.
3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

Related topics: Math, String

Similar questions: #066PlusOne, #067AddBinary
'''
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = [0]*(len(num1) + len(num2))
        # Calculation
        for i in range(len(num1)):
            for j in range(len(num2)):
                num = res[i+j] + (int(num1[i])*int(num2[j]))
                asce_num, stay_num = divmod(num, 10)
                res[i+j] = stay_num
                res[i+j+1] += asce_num
        # Skip the unecessary zero
        i = len(res) - 1
        while i > 0 and res[i] == 0:
            i -= 1

        return ''.join(map(str, res[i::-1]))

if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    sol = Solution()
    print(sol.multiply(num1, num2))