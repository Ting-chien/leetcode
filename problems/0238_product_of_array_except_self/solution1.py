from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Division operator in not allowed in this problem ❌
        """
        
        # Get product of all elements
        product = reduce(lambda x, y: x * y, nums)

        # Divided all elements by product
        ans = map(lambda x: int(product/x) if product else 0, nums)

        return list(ans)
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Get prefix product
        prefix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[i]*nums[i])

        # Get postfix product
        postfix = [1]
        for i in range(len(nums)-1, -1, -1):
            postfix.append(postfix[len(nums)-i-1]*nums[i])

        # Use reverse instead insert every element from left side of list
        # can have better complexity, since complexity of insert(0, num) is
        # O(n) and reverse() is also O(n).
        postfix.reverse() 

        # Iterate through prefix and postfix to get product
        product = []
        for i in range(len(nums)):
            product.append(prefix[i]*postfix[i+1])

        return product
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Improve space complexity
        """
        ans = []
        # Get prefix of product
        prefix = 1
        for i in range(len(nums)):
            ans.append(prefix)
            prefix = prefix * nums[i]

        # Calcualte result from the reverse direction
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * postfix
            postfix = postfix * nums[i]

        return ans
    

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
res = Solution().productExceptSelf(nums = [1,2,3,4])
print(res)

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
res = Solution().productExceptSelf(nums = [-1,1,0,-3,3])
print(res)