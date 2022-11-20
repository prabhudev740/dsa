package main

import "fmt"

func main() {
	fmt.Println("Recursion")
	n := 5
	treeRecursion(n)
}

func headRecursion(n int) {
	if n > 0 {
		headRecursion(n - 1)
		fmt.Println(n)
	}
}

func tailRecursion(n int) {
	if n > 0 {
		fmt.Println(n)
		tailRecursion(n - 1)
	}
}

func treeRecursion(n int) {
	if n > 0 {
		fmt.Println(n)
		treeRecursion(n - 1)
		fmt.Println(n)
	}
}
