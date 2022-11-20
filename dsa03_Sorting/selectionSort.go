package main

import (
	"fmt"
)

func main() {
	fmt.Println("Selection Sort")
	arr := []int{3, 5, 8, 9, 6, 2}
	fmt.Println(arr)
	selectionSort(arr)
	fmt.Println(arr)
}

func selectionSort(arr []int) {
	fmt.Println("")
	var pos int
	n := len(arr)

	for i := 0; i < n; i++ {
		pos = i

		for j := i + 1; j < n; j++ {
			if arr[j] < arr[pos] {
				pos = j
			}
		}
		arr[i], arr[pos] = arr[pos], arr[i]
	}
}
