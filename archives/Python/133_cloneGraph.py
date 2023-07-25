from pprint import pprint

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return node

        queue = [node]
        visited = {node: Node(node.val)}

        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]

class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node: return node

        visited = {node: Node(node.val)}

        def dfs(node: 'Node') -> 'Node':

            nonlocal visited

            if not node: return node

            if node in visited: return visited[node]

            copy_node = Node(node.val)
            visited[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))

            return copy_node

        return dfs(node)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    sol = Solution1()
    pprint(vars(sol.cloneGraph(node1)))