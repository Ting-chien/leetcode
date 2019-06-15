'''
Given a non-empty array of digits representing a non-negative integer, 
plus one to the integer. The digits are stored such that the most 
significant digit is at the head of the list, and each element in the 
array contain a single digit. You may assume the integer does not contain 
any leading zero, except the number 0 itself.

Related topics: Array

Similar questions: Add binary, Plus One Linked List, Add to Array-form of Integer
'''
class Solution:
    def plusOne1(self, digits):
        """
        Method:
        Complexity: O(n)
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        digits = digits[::-1]
        for i in range(len(digits)):
            digits[i] += carry
            carry, digits[i] = divmod(digits[i], 10)
        if carry == 1:
            digits.append(carry)

        return digits[::-1]

    def plusOne2(self, digits):
        """
        Method:
        Complexity: O(n)
        :type digits: List[int]
        :rtype: List[int]
        """
        # 不讓迴圈全部跑完，當該位數+1後不進位時直接返回答案
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        # 若是到最後還有進位，直接在串列最前端補一個1
        digits.insert(0, 1)

        return digits

if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne2([1, 2, 3]))
    print(sol.plusOne2([9, 9, 9]))