class Solution:

    def convert_to_base7(self, num: int) -> str:
        
        is_positive = num > 0
        
        res = ""
        while num != 0:
            num, mod = divmod(abs(num), 7)
            res = str(mod) + res

        return res if is_positive else "-" + res


if __name__ == '__main__':
    sol = Solution()
    print(sol.convert_to_base7(100))
    print(sol.convert_to_base7(-7))
    print(sol.convert_to_base7(20))