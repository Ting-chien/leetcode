package main

import (
	"fmt"
)

func maxProduct(nums []int) int {
    currMax, currMin := nums[0], nums[0]
    res := currMax

    for i := 1; i < len(nums); i++ {
        num := nums[i]
        prevMax, prevMin := currMax, currMin

        currMax = max(prevMax*num, prevMin*num, num)
        currMin = min(prevMax*num, prevMin*num, num)

        res = max(res, currMax)
    }

    return res
}


func main() {
	// 自己準備幾筆測試資料直接執行
	tests := [][]int{
		{2, 3, -2, 4},     // 預期 6
		{-2, 0, -1},       // 預期 0
		{-2, 3, -4},       // 預期 24
		{0, 2},            // 預期 2
		{-2},              // 預期 -2
	}

	for _, nums := range tests {
		fmt.Println(nums, " => ", maxProduct(nums))
	}
}