package main

import (
	"fmt"
)

func main() {
	fmt.Println("Merge Sort")
	arr := []int{3, 5, 8, 9, 6, 2, 1, -1}
	fmt.Println(arr)
	mergeSort(arr, 0, len(arr)-1)
	fmt.Println(arr)
}

func mergeSort(arr []int, left, right int) {
	if left < right {
		mid := int((left + right) / 2)
		mergeSort(arr, left, mid)
		mergeSort(arr, mid+1, right)
		merge(arr, left, mid, right)
	}
}

func merge(arr []int, left, mid, right int) {
	i, j := left, mid+1

	temp := []int{}

	for i <= mid && j <= right {
		if arr[i] <= arr[j] {
			temp = append(temp, arr[i])
			i++
		} else {
			temp = append(temp, arr[j])
			j++
		}
	}

	if i <= mid {
		temp = append(temp, arr[i:mid+1]...)
	}

	if j <= right {
		temp = append(temp, arr[j:right+1]...)
	}

	for i, v := range temp {
		arr[i+left] = v
	}
}
