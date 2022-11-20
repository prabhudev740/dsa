package main

import "fmt"

func main() {
	fmt.Println("Binary tree")
	T := BinaryTree{}
	left := BinaryTree{}
	right := BinaryTree{}
	left.makeTree(20, nil, nil)
	right.makeTree(30, nil, nil)
	T.makeTree(10, &left, &right)
	T.inorder(T.root)
	fmt.Println(T.root.left)

	// left := TreeNode{}
	// right := TreeNode{}
	// T := BinaryTree{}

	// left := makeTree(20, nil, nil)
	// right := makeTree(30, nil, nil)
	// T := makeTree(10, &left, &right)

	// fmt.Printf("%T", T)
	// fmt.Println(T.element)
	// fmt.Println(T.left.element)
	// fmt.Println(T.right.element)

	// T.preorder()
}

type TreeNode struct {
	element int
	left    *TreeNode
	right   *TreeNode
}

type BinaryTree struct {
	root *TreeNode
}

// func makeTree(element int, left *TreeNode, right *TreeNode) TreeNode {
// 	return TreeNode{element, left, right}
// }
func (B BinaryTree) makeTree(element int, left *BinaryTree, right *BinaryTree) {
	B.root = &TreeNode{element, left.root, right.root}
}

func (T *TreeNode) preorder() {
	if T != nil {
		fmt.Print(T.element, " ")
		T.left.preorder()
		T.right.preorder()
	}
}

func (B BinaryTree) inorder(root *TreeNode) {
	if root != nil {
		B.inorder(root.left)
		fmt.Println(root.element)
		B.inorder(root.right)
	}
}

func (B TreeNode) postorder(root *TreeNode) {
	if root != nil {
		B.postorder(root.left)
		B.postorder(root.right)
		fmt.Println(root.element)
	}
}
