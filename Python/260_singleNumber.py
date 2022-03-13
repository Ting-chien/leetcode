from tkinter import N
from typing import List

class Solution1:
    def singleNumber(self, nums: List[int]) -> List[int]:

        if len(nums) == 2: return nums
        
        # Iterate all elements in nums and save into d
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # Iterate all key-value pair in d
        res = []
        for k, v in d.items():
            if v == 1:
                res.append(k)

        return res

class Solution2:
    '''
    Bit manipulation 詳細版
    '''
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # 將數組內所有資料跑過一輪異或得到只出現一次的兩個數的異或
        mask = 0
        for num in nums:
            mask ^= num

        # 找出此異或結果最右側為1的位置(因為1即代表兩個不同位元異或的結果)
        diff = 1
        while mask & diff == 0:
            diff = diff << 1

        # 再次將所有數值進行異或，但前置動作要先透過diff將數組分為兩組
        res = [0, 0]
        for num in nums:
            # 包含其中一個答案的數組（在diff是0）
            if num&diff == 0:
                res[0] ^= num
            # 包含另一個答案的數組（在diff也是1）
            else:
                res[1] ^= num

        return res

class Solution3:
    '''
    Bit manipulation 精簡版
    '''
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # 一樣先將數組內所有資料跑過一輪異或得到只出現一次的兩個數的異或
        mask = 0
        for num in nums:
            mask ^= num

        # 一樣找出此異或結果最右側為1的位置，但可利用正負數值在AND運算的特性找到
        diff = mask & -mask

        # 剩下的操作與詳細版本類似，但在求得其中一個答案後直接將該答案與mask做異或即可求得另一組解
        n = 0
        for num in nums:
            # 包含其中一個答案的數組，即 True=1
            if num&diff:
                n ^= num

        return [n, n^mask]

if __name__ == '__main__':
    sol = Solution3()
    ans1 = sol.singleNumber([1,2,1,3,2,5])
    print(ans1)
    ans2 = sol.singleNumber([-1,0])
    print(ans2)
    ans3 = sol.singleNumber([0,1])
    print(ans3)