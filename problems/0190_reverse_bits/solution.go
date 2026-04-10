package main

import (
	"fmt"
)


func reverseBits(n int) int {
    var res int = 0
	for i := 0; i < 32; i++ {
		res = (res << 1) | (n & 1)
		n >>= 1
	}
	return  res
}



func main() {
	// Case 1. 
	// Input: n = 43261596
	// Output: 964176192
	n := 43261596
	fmt.Print("Case 1: ", reverseBits(n))
}