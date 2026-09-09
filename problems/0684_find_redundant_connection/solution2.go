package main

import "fmt"

func findRedundantConnection(edges [][]int) []int {
    
    n := len(edges)
    count := n
    parent := make([]int, n+1)
    for i := 0; i <= n; i++ {
        parent[i] = i
    }

    var find func(x int) int
    find = func(x int) int {
        if x != parent[x] {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    var union func(x, y int) bool
    union = func(x, y int) bool {
        rootX := find(x)
        rootY := find(y)
        if rootX != rootY {
            parent[rootY] = rootX
            count--
            return true
        }
        return false
    }

    for _, edge := range edges {
        node1, node2 := edge[0], edge[1]
        if !union(node1, node2) {
            return []int{node1, node2}
        }
    }
    
    return nil
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
