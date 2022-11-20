package main

import (
	"fmt"
)

func main() {
	fmt.Println("Inseration Sort")
	arr := []int{3, 5, 8, 9, 6, 2}
	fmt.Println(arr)
	inssertionSort(arr)
	fmt.Println(arr)
}

func inssertionSort(arr []int) {
	n := len(arr)
	var cur, pos int

	for i := 0; i < n; i++ {
		cur = arr[i]
		pos = i

		for pos > 0 && arr[pos-1] > cur {
			arr[pos] = arr[pos-1]
			pos--
		}
		arr[pos] = cur
	}
}
