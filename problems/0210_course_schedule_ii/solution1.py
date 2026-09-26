from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        # Turn the courses dependency to a directly graph, and
        # count the indegree (number of prerequisites) for each course
        graph = defaultdict(list)
        deg = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            deg[u] += 1

        # Find available course
        queue = deque()
        for course, indegree in enumerate(deg):
            if indegree == 0:
                queue.append(course)

        ans = []
        while queue:
            prerequisite = queue.popleft()
            ans.append(prerequisite)
            for course in graph.get(prerequisite, []):
                deg[course] -= 1
                if deg[course] == 0:
                    queue.append(course)

        return ans if len(ans) == numCourses else []


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print(solution.findOrder(numCourses=2, prerequisites=[[1, 0]]))  # [0, 1]

    # Example 2
    print(solution.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0, 2, 1, 3]

    # Example 3
    print(solution.findOrder(numCourses=1, prerequisites=[]))  # [0]
