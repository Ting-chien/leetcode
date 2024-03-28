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
    
    def fizzBuzz(self, n: int) -> List[str]:
        """字串組裝
        Solution1 的做法在遇到更多的判斷條件時，要建立
        的if-else statement會變得非常多，透過字串的組裝
        可以解決部分的問題。
        """
        res = []
        for i in range(1, n+1):
            char = ""
            is_divisible = False
            if i % 3 == 0:
                char += "Fizz"
                is_divisible = True
            if i % 5 == 0:
                char += "Buzz"
                is_divisible = True
            if not is_divisible:
                char += str(i)
            res.append(char)
        return res
    
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