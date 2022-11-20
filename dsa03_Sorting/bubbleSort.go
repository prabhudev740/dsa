package main

import (
	"fmt"
)

func main() {
	fmt.Println("Bubble Sort")
	arr := []int{3, 5, 8, 9, 6, 2}
	fmt.Println(arr)
	bubbleSort(arr)
	fmt.Println(arr)
}

func bubbleSort(arr []int) {
	n := len(arr)
	var isSorted bool
	for pass := n - 1; pass >= 0; pass-- {
		isSorted = true

		for i := 0; i < pass; i++ {
			if arr[i] > arr[i+1] {
				arr[i], arr[i+1] = arr[i+1], arr[i]
				isSorted = false
			}
		}
		if isSorted {
			break
		}

	}
}
