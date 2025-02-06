from typing import List
from itertools import combinations
from collections import defaultdict


class Solution1:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """ (Time Limit Exceed)
        1. Choose four numbers from the list
        2. Check if the product of the first two numbers is equal to the product of the last two numbers
        3. If so, increment the count
        """
        def equal(arr: List[int]) -> bool:
            pairs = list(combinations(arr, 2))  # Generate all pairs
            products = {x * y for x, y in pairs}  # Compute unique products
            return len(products) < len(pairs)  # If duplicates exist, some pairs have equal products
        cnt = 0
        def dfs(s: int, curr: List[int]):
            if len(curr) == 4:
                if equal(curr):
                    nonlocal cnt
                    cnt += 8
                return
            if s == len(nums):
                return
            for i in range(s, len(nums)):
                dfs(i+1, curr+[nums[i]])
        dfs(0, [])
        return cnt
    

class Solution2:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Btutal Force (Time Limit Exceed)
        1. 因為要符合 a*b == c*d 條件，因此一定要有一小一大的值存在，
        所有可透過左、右指針從 nums 兩側向中間聚合
        2. 接著在遍歷左、右指針中間的數值得到 c，如果 a*b/c 存在 nums，
        則代表是一個可行的組合
        """
        # 因為要從左右先取得 a,b，所以要先將 nums 排序
        nums.sort()

        N = len(nums)
        cnt = 0
        for _a in range(N):
            for _b in range(N-1, _a, -1):
                # 如果 _b, _b 之間含有至少兩個數字才有需要繼續遍歷
                if (_b - _a) >= 3:
                    a, b = nums[_a], nums[_b]
                    product = a * b
                    possible_d_values = set(nums[_a+1:_b])
                    for _c in range(_a+1, _b):
                        c = nums[_c]
                        possible_d_values.remove(c)
                        if product % c == 0:
                            d = product // c
                            if d in possible_d_values:
                                cnt += 8

        return cnt
    

class Solution3:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 找出所有兩兩相乘的乘積
        N = len(nums)
        product_pairs = [nums[i]*nums[j] for i in range(N) for j in range(i+1, N)]
        # 計算每組乘積出現的次數
        counter = defaultdict(int)
        for product in product_pairs:
            counter[product] += 1
        # 根據每組乘積出現的次數，來計算排列組合的組數
        # e,g,. [6, 8, 12, 12, 18, 24] 中有兩組 12 一樣，因此組合有 (2-1)*2//2=1 組
        # 而一組裡面有 8 種排列組合 (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3) , (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
        cnt = 0
        for val in counter.values():
            num_of_pairs = ((val-1)*val) // 2
            cnt += num_of_pairs*8
        return cnt

    

# Example 1:
# Input: nums = [2,3,4,6]
# Output: 8
res = Solution3().tupleSameProduct([2,3,4,6])
print(res) # Expected: 8

# Example 2:
# Input: nums = [1,2,4,5,10]
# Output: 16
res = Solution3().tupleSameProduct([1,2,4,5,10])
print(res) # Expected: 16