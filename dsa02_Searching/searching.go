package main

import (
	"fmt"
	// "math"
)

func main() {
	arr := []int{1, 2, 3, 4, 5}
	arr1 := []int{5, 4, 3, 2, 1}
	// fmt.Println(lenearSearch(arr, 5))
	// fmt.Println(binarySearchAsc(arr, 1))
	// fmt.Println(binarySearchDesc(arr1, 1))
	fmt.Println(binarySearchAny(arr, 3))
	fmt.Println(binarySearchAny(arr1, 3))
	fmt.Println(binarySearchRecursion(arr, 0, len(arr)-1, 4))
}

func lenearSearch(arr []int, key int) int {
	fmt.Println("Lenear Searching")
	for i, v := range arr {
		if key == v {
			return i
		}
	}
	return -1
}

func binarySearchAsc(arr []int, key int) int {
	s := 0
	e := len(arr) - 1
	var mid int

	for s <= e {
		mid = int((s + e) / 2)
		if arr[mid] == key {
			return mid
		} else if arr[mid] > key {
			e = mid - 1
		} else {
			s = mid + 1
		}
	}
	return -1
}

func binarySearchDesc(arr []int, key int) int {
	s := 0
	e := len(arr) - 1
	var mid int

	for s <= e {
		mid = int((s + e) / 2)

		if arr[mid] == key {
			return mid
		} else if arr[mid] > key {
			s = mid + 1
		} else {
			e = mid - 1
		}
	}
	return -1
}

func binarySearchAny(arr []int, key int) int {
	s := 0
	e := len(arr) - 1
	var mid int
	isAsc := arr[s] < arr[e]

	for s <= e {
		mid = int((s + e) / 2)

		if arr[mid] == key {
			return mid
		} else if isAsc {
			if arr[mid] > key {
				e = mid - 1
			} else {
				s = mid + 1
			}
		} else {
			if arr[mid] > key {
				s = mid + 1
			} else {
				e = mid - 1
			}
		}
	}

	return -1
}

func binarySearchRecursion(arr []int, s, e, key int) int {
	if s > e {
		return -1
	}
	mid := int((s + e) / 2)
	if arr[mid] == key {
		return mid
	} else if arr[mid] < key {
		return binarySearchRecursion(arr, mid+1, e, key)
	} else {
		return binarySearchRecursion(arr, s, mid-1, key)
	}
}
