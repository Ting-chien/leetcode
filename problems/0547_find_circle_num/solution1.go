package main

import "fmt"

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	visited := make([]bool, n)

	var dfs func(city int)
	dfs = func(city int) {
		for next := 0; next < n; next++ {
			if isConnected[city][next] == 1 && !visited[next] {
				visited[next] = true
				dfs(next)
			}
		}
	}

	provinces := 0
	for city := 0; city < n; city++ {
		if !visited[city] {
			provinces++
			visited[city] = true
			dfs(city)
		}
	}

	return provinces
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
