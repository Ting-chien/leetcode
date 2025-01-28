from typing import List
from collections import defaultdict


class Solution1:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # Transfer 2D array into a hash map
        prerequisites_map = defaultdict(list)
        for c1, c2 in prerequisites:
            prerequisites_map[c1].append(c2)

        # Go through queries and check if the pair is prerequisite of one another
        ans = []
        for c1, c2 in queries:
            # 透過一個 map 來紀錄是否已找過該門課
            visited = [False] * numCourses
            # 透過一個 queue 來紀錄要被查詢的課程
            queue = [c1]
            is_prerequisite = False
            while queue:
                # 取出一門課程，查看該門課是哪些課程的先修課
                pre_c = queue.pop(0)
                # 若已經查過該門課，則跳過
                if visited[pre_c]:
                    continue
                visited[pre_c] = True
                courses =prerequisites_map.get(pre_c)
                # 在這些課程中確認是否包含 c2，若找不到則從該門課再往下找尋
                if courses:
                    for course in courses:
                        if course == c2:
                            is_prerequisite = True
                            break
                        queue.append(course)
            # 紀錄 c1 是否為 c2 的先修課
            ans.append(is_prerequisite)

        return ans
    

class Solution2:

    def checkIsPrerequisite(self, prerequisites: dict, visited: dict, c1: int, c2: int):
        visited[c1] = True
        if c1 == c2:
            return True
        
        for c in prerequisites.get(c1, []):
            if not visited[c]:
                if self.checkIsPrerequisite(prerequisites, visited, c, c2):
                    return True
                
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Solution 2: DFS
        """
        # Transfer 2D array into a hash map
        prerequisites_map = defaultdict(list)
        for c1, c2 in prerequisites:
            prerequisites_map[c1].append(c2)

        ans = []
        for c1, c2 in queries:
            visited = [False] * numCourses
            is_prerequisite = self.checkIsPrerequisite(prerequisites_map, visited, c1, c2)
            ans.append(is_prerequisite)

        return ans
    

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
res = Solution2().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])
print(res) # [false,true]

# Example 2:
# Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
res = Solution2().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])
print(res) # [false,false]

# Example 3:
# Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
res = Solution2().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
print(res) # [true,true]