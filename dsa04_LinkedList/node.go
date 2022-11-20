package main

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

func main() {
	fmt.Println("----Node----")
	x := Node{30, nil}
	y := Node{20, &x}
	z := Node{10, &y}

	temp := &z

	for temp != nil {
		fmt.Println(temp.val, "->")

		temp = temp.next
	}
}
