package main

import "fmt"

func find(parents []int, x int) int {
	if parents[x] != x {
		parents[x] = find(parents, parents[x])
	}
	return parents[x]
}

func union(parents []int, count *int, x, y int) {
	rootX := find(parents, x)
	rootY := find(parents, y)
	if rootX != rootY {
		parents[rootY] = rootX
		*count--
	}
}

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	parents := make([]int, n)
	for i := 0; i < n; i++ {
		parents[i] = i
	}
	count := n

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if isConnected[i][j] == 1 {
				union(parents, &count, i, j)
			}
		}
	}

	return count
}

func main() {
	// Example 1:
	// Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
	// Output: 2
	fmt.Println(findCircleNum([][]int{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}))

	// Example 2:
	// Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
	// Output: 3
	fmt.Println(findCircleNum([][]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}))

	// Example 3:
	// Input: isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
	// Output: 1
	fmt.Println(findCircleNum([][]int{
		{1, 0, 0, 1},
		{0, 1, 1, 0},
		{0, 1, 1, 1},
		{1, 0, 1, 1},
	}))
}
