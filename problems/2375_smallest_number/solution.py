from typing import List


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        使用 dfs 來遍歷 1~9 數字所有可能的排列組合，並找出
        最小值
        """
        nums = [i+1 for i in range(len(pattern)+1)]
        N = len(nums)
        min_num = float('inf')
        def valid(a, b, p):
            """
            Arg:
                a: nums[i]
                b: nums[i+1]
                p: I or D
            """
            # print(f"a={type(a)}, b={type(b)}")
            if p == "I":
                return a < b
            if p == "D":
                return a > b
        def dfs(remain: List[int], curr: str):
            """
            Args:
                remain: 剩餘的數字
                curr: 現在組成的數字
            """
            print(f"remain={remain}, curr={curr}")
            if len(remain) == 0:
                min_num = min(min_num, curr)
                return
            for i in range(len(remain)):
                print(f"pattern={pattern}")
                p = pattern[len(str(curr))-1]
                if valid(int(curr[-1]), remain[i], p):
                    dfs(remain[:i]+remain[i+1:], curr+str(remain[i]))
        dfs(nums, "0")




# Example 1:
# Input: pattern = "IIIDIDDD"
# Output: "123549876"
res = Solution().smallestNumber("IIIDIDDD")
print(res)