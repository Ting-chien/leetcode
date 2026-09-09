package main

import "fmt"

func findRedundantConnection(edges [][]int) []int {
    // Initialize a graph to store relation between vertex
    graph := make(map[int][]int)
    // During traveling, if two vertices already connected, return directly
    for _, edge := range edges {
        node1, node2 := edge[0], edge[1]
        if isConnected(node1, node2, make(map[int]struct{}), graph) {
            return []int{node1, node2}
        }
        graph[node1] = append(graph[node1], node2)
        graph[node2] = append(graph[node2], node1)
    }
    return nil
}

func isConnected(node1, node2 int, visited map[int]struct{}, graph map[int][]int) bool {
    // If two nodes are identical, return true for connected
    if node1 == node2 {
        return true
    }
    // Mark as visited
    visited[node1] = struct{}{}
    // Travel through adjacent nodes
    for _, node := range graph[node1] {
        _, exist := visited[node]
        if !exist && isConnected(node, node2, visited, graph) {
            return true
        }
    }
    return false
}

func main() {
	// Example 1:
	// Input: edges = [[1,2],[1,3],[2,3]]
	// Output: [2,3]
	fmt.Println(findRedundantConnection([][]int{{1, 2}, {1, 3}, {2, 3}}))

	// Example 2:
	// Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
	// Output: [1,4]
	fmt.Println(findRedundantConnection([][]int{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}}))
}
