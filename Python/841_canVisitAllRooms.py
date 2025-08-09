from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Use an array to store if we have visited the room, and 
        visit each room with the keys find in the room
        
        Approach
        1. Initiallize an array with length = N
        2. Iterate throuhg rooms and get keys
        3. Iterate keys and visit the room with key
        4. Return if all room are visited

        Complexity
        * Time: O(n) - beats 100%
        * Space: O(n) - beats 47.72%
        """
        visited = [False for _ in range(len(rooms))]

        def dfs(keys: List[int]):
            for key in keys:
                if not visited[key]:
                    visited[key] = True
                    dfs(keys=rooms[key])

        dfs(keys=[0])
        return all(visited)
    

# Example 1:
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# keys=[0], 
#     key=0, visited=[T,F,F,F], keys=[1]
#         keys=[1]
#             key=1, visited=[T,T,F,F], keys=[2,3]
#                 key=2, visited=[T,T,T,F], no key
#                 key=3, visited=[T,T,T,T], no key
res = Solution().canVisitAllRooms([[1],[2],[3],[]])
print(res)

# Example 2:
# Input: rooms = [[1],[2,3],[],[]]
# Output: true
res = Solution().canVisitAllRooms([[1],[2,3],[],[]])
print(res)

# Example 2:
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
res = Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
print(res)