from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        1. 算出 missing rolls 的加總為何？
        2. 把剩餘的點數平均分配到 n 個位置去
        """
        # Get sum of missing rolls
        remain = (len(rolls)+n)*mean - sum(rolls)

        # Check if remain is separable
        if remain < n or remain > 6*n: return []

        # Separate remain into n missing rolls
        div, mod = divmod(remain, n)
        missing = [div]*n
        for i in range(mod):
            missing[i] += 1

        return missing
    

if __name__ == '__main__':

    # Example 1
    # Input: rolls = [3,2,4,3], mean = 4, n = 2
    # Output: [6,6]
    print(Solution().missingRolls(rolls=[3,2,4,3], mean=4, n=2))

    # Example 2
    # Input: rolls = [1,5,6], mean = 3, n = 4
    # Output: [2,3,2,2]
    print(Solution().missingRolls(rolls=[1,5,6], mean=3, n=4))

    # Example 3
    # Input: rolls = [1,2,3,4], mean = 6, n = 4
    # Output: []
    print(Solution().missingRolls(rolls=[1,2,3,4], mean=6, n=4))