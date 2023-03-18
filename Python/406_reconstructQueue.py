from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        # sort the people by h reversely and k advencelly
        people.sort(key=lambda x: (-x[0], x[1]))

        # insert each set into correct position by second index
        res = []
        for p in people:
            res.insert(p[1], p)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
    print(sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))