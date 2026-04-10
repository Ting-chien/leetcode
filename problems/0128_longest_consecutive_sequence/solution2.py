from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        # Change root_x and root_y to make sure union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parents[root_y] = root_x
        self.size[root_x] += self.size[root_y]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Use Union Find to find the longest consecutive sequence.

        The idea of find the LCS by Union Find is take each number
        as a node in uf. If number x and x+1 both exist in nums, we
        should connect them to a group.

        For example, nums=[2,20,4,10,3,4,5]

            Step 1. Remove duplicate number in nums

                dict = {2:0,20:1,4:2,10:3,3:4,5:6}

            Step 2. Iterate through the dict and group the consecutive
            number.

                uf.parent = [0, 1, 0, 3, 0, 5, 2]
                uf.size = [4, 1, 2, 1, 1, 1, 1]

                num=2, num+1 exist, union(0,4)
                => parent[4] = 0, size[0] = 2

                num=20, num+1 not exist

                num=4, num+1 exist, union(2,6)
                => parent[6] = 2, size[2] = 2

                num=10, num+1 not exist

                num=3, num+1 exist, union(4,2)
                => root_x=0, root_y=2, parent[2] = 0, size[0] = 4
        """

        if not nums: return 0

        # Record the number and index
        num_to_index = {}
        for i, num in enumerate(nums):
            if num in num_to_index:
                continue
            num_to_index[num] = i

        # Grouping
        uf = UnionFind(n=len(nums))
        for num, i in num_to_index.items():
            # Group two number's index if x and x+1 exist
            if num + 1 in num_to_index:
                uf.union(i, num_to_index[num+1])

        # Return the maximum value of size
        return max(uf.size)


