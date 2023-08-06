from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                res.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                res.append("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i))

        return res


if __name__ == '__main__':

    sol = Solution()

    # Test 1
    print(sol.fizzBuzz(n=3))

    # Test 2
    print(sol.fizzBuzz(n=5))

    # Test3 
    print(sol.fizzBuzz(n=15))