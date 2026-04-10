from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        cnt = 1
        for i, char in enumerate(chars):
            if i == 0:
                res.append(char)
            else:
                if chars[i] == chars[i-1]:
                    cnt += 1
                else:
                    res += list(str(cnt))
                    res.append(char)
                    cnt = 1
        if cnt > 1: res += list(str(cnt))
        chars = res + chars
        return res
    
class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Use two pointers, one is to iterate through array
        and group letters, the other one is to write answer
        back to array
        """
        read = 0
        write = 0
        while read < len(chars):
            letter = chars[read]
            cnt = 0
            while read < len(chars) and chars[read] == letter:
                cnt += 1
                read += 1
            # Write letter back to chars
            chars[write] = letter
            write += 1
            # Write cnt back to chars
            if cnt > 1:
                for c in str(cnt):
                    chars[write] = c
                    write += 1
        return chars


# Example 1:
res = Solution().compress(["a","a","b","b","c","c","c"])
print(res) # ["a","2","b","2","c","3"]

# Example 2:
res = Solution().compress(["a"])
print(res) # ["a"]

# Example 3:
res = Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print(res) # ["a","b","1","2"]