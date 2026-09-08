package main

import "fmt"

func canVisitAllRooms(rooms [][]int) bool {
	visited := make([]bool, len(rooms))

	var dfs func(keys []int)
	dfs = func(keys []int) {
		for _, key := range keys {
			if !visited[key] {
				visited[key] = true
				dfs(rooms[key])
			}
		}
	}

	dfs([]int{0})
	for _, v := range visited {
		if !v {
			return false
		}
	}
	return true
}

func main() {
	// Example 1:
	// Input: rooms = [[1],[2],[3],[]]
	// Output: true
	fmt.Println(canVisitAllRooms([][]int{{1}, {2}, {3}, {}}))

	// Example 2:
	// Input: rooms = [[1,3],[3,0,1],[2],[0]]
	// Output: false
	fmt.Println(canVisitAllRooms([][]int{{1, 3}, {3, 0, 1}, {2}, {0}}))
}
