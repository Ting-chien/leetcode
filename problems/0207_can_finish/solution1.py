from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # Turn the prerequisites into a map and record its degree
        graph = defaultdict(list) # Prerequisites for each course
        indegree = [0] * numCourses # How many prerequisites left for course i

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        # Push all source(degree=0) into a queue
        queue = deque()
        for idx, degree in enumerate(indegree):
            if degree == 0:
                queue.append(idx)

        # Start from source and visit their prerequisites
        count = 0
        while queue:
            prerequisite = queue.popleft()
            count += 1
            for course in graph.get(prerequisite, []):
                # Substract 1 for taking one prerequisite done
                indegree[course] -= 1
                # If all prerequisites done, course can be taken
                if indegree[course] == 0:
                    queue.append(course)

        return count == numCourses