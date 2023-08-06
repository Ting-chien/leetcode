from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """Hash
        如果條件實在太多時，可以用hash map把條件存起來再去做遍歷
        """
        res = []
        d = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n+1):
            char = ""
            is_divisible = False
            for k, v in d.items():
                if i % k == 0:
                    char += v
                    is_divisible = True
            if not is_divisible:
                char += str(i)
            res.append(char)
        return res
    

if __name__ == '__main__':

    sol = Solution()

    # Test 1
    print(sol.fizzBuzz(n=3))

    # Test 2
    print(sol.fizzBuzz(n=5))

    # Test3 
    print(sol.fizzBuzz(n=15))