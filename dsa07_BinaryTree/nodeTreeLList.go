package main

import "fmt"

func main() {
	fmt.Println("Tree Node")
	left := TreeNode{20, nil, nil}
	right := TreeNode{30, nil, nil}
	root := TreeNode{10, &left, &right}

	display(&root)
	// fmt.Println(three.)
}

type TreeNode struct {
	element int
	left    *TreeNode
	right   *TreeNode
}

func display(root *TreeNode) {
	if root != nil {
		fmt.Println(root.element)
		display(root.left)
		display(root.right)
	}
}
