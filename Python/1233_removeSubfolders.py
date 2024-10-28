from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 將folder按照長度和字母順序排列，因此子路徑必會在原路徑之後
        folder.sort()
        # 由folder的第一個路徑往後做比對
        res = [folder[0]]
        for i in range(1, len(folder)):
            last_folder = res[-1] + "/"
            if not folder[i].startswith(last_folder):
                res.append(folder[i])
        return res


# Example 1:
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
res = Solution().removeSubfolders(["/c/d","/c/d/e","/c/f","/a","/a/b"])
print(res)

# Example 2:
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
res = Solution().removeSubfolders(["/a/b/d","/a","/a/b/c"])
print(res)

# Example 3:
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
res = Solution().removeSubfolders(["/a/b/ca","/a/b/c","/a/b/d"])
print(res)